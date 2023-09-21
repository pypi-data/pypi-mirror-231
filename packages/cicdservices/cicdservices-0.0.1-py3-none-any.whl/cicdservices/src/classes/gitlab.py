import os
import subprocess
import time

import git
import gitlab
import urllib3
from decouple import config

from ..Interfaces.git import RepoAPI

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class GitLabAPI(RepoAPI):
    def __init__(self, token: str):
        self.gl = gitlab.Gitlab(
            "https://gitlab.com/", oauth_token=token, api_version=4, ssl_verify=False
        )

    def search_group(self, group_name: str):
        try:
            gitlab_group = self.gl.groups.list(search=group_name)[0]
            return gitlab_group
        except Exception as err:
            raise Exception(f"Error al buscar el grupo: {err}")

    def create_repo(self, repo_name: str, group: str = None, template: str = None):
        try:
            new_repo = None
            if group:
                new_repo = group.create_repository({"name": repo_name})
                new_repo = self.gl.projects.create({"name": repo_name})
                data = {
                    "branch": "main",
                    "commit_message": f"First upload on repo {repo_name}",
                    "actions": [
                        {
                            "action": "create",
                            "file_path": "./README.md",
                            "content": f"First upload on repo {repo_name}",
                        },
                    ],
                }
                new_repo.commits.create(data)
            else:
                new_repo = self.gl.projects.create({"name": repo_name})
                data = {
                    "branch": "main",
                    "commit_message": f"First upload on repo {repo_name}",
                    "actions": [
                        {
                            "action": "create",
                            "file_path": "./README.md",
                            "content": f"First upload on repo {repo_name}",
                        },
                    ],
                }
                new_repo.commits.create(data)
            if template:
                new_repo.repository_tree.create(
                    {"path": "/", "branch": "master"}, template.id, "master"
                )
            return new_repo
        except Exception as err:
            raise Exception(f"Error al crear el projecto: {err}")

    def add_users_to_repo(self, repo: str, emails: str):
        try:
            repo = self.gl.projects.get(id=repo)
            user = self.gl.users.get(id=emails)
            repo.members.create(
                {"user_id": user.id, "access_level": gitlab.const.AccessLevel.DEVELOPER}
            )
            return repo
        except Exception as err:
            raise Exception(f"Error al agregar usuario al repositorio: {err}")

    def get_statistics(self, repo_name: str, emails: str):
        try:
            repo = self.gl.projects.get(repo_name)
            commit_count = 0
            merge_request_count = 0
            merge_request_changes_count = 0
            merge_request_comment_count = 0
            for email in emails:
                commits = repo.commits.list(author_email=email)
                commit_count += len(commits)
                merge_requests = repo.mergerequests.list(author_email=email)
                merge_request_count += len(merge_requests)
                for mr in merge_requests:
                    merge_request_changes_count += mr.changes_count
                    merge_request_comment_count += mr.notes.list().total
            return {
                "commits": commit_count,
                "merge_request_comments": merge_request_comment_count,
                "merge_request_changes": merge_request_changes_count,
                "merge_requests": merge_request_count,
            }
        except repo.DoesNotExist:
            return False

    def create_or_update_pull_request(
        self,
        repo_name: str,
        title: str,
        body: str,
        head: str,
        base: str,
        reviewers=None,
        assignee=None,
        labels=None,
        state=None,
    ):
        try:
            repo = self.gl.projects.get(repo_name)
            pull_requests = repo.mergerequests.list(state="opened")
            pull_request = None
            for pr in pull_requests:
                if pr.title == title:
                    pull_request = pr
                    break
            if pull_request:
                pull_request.title = title
                pull_request.description = body
                pull_request.source_branch = head
                pull_request.target_branch = base
                if reviewers:
                    pull_request.reviewers = reviewers
                if assignee:
                    pull_request.assignee = assignee
                if labels:
                    pull_request.labels = labels
                if state:
                    pull_request.state = state
                pull_request.save()
            else:
                pull_request = repo.mergerequests.create(
                    {
                        "title": title,
                        "description": body,
                        "source_branch": head,
                        "target_branch": base,
                        "reviewers": reviewers,
                        "assignee": assignee,
                        "labels": labels,
                        "state": state,
                    }
                )
            return True
        except repo.DoesNotExist:
            return False

    def remove_users_from_repo(self, repo_name: str, emails: str):
        try:
            repo = self.gl.projects.get(id=repo_name)
            user = self.gl.users.get(id=emails)
            repo.members.delete(user.id)
            return user.id
        except Exception as err:
            raise Exception(f"Error al eliminar usuario al repositorio: {err}")

    def update_repo(
        self, repo_name: str, new_name: str = None, new_description: str = None
    ):
        try:
            repo = self.gl.projects.get(id=repo_name)
            if new_name:
                repo.name = new_name
            if new_description:
                repo.description = new_description
            repo.save()
            update_repo = self.gl.projects.get(id=repo_name)
            return update_repo
        except Exception as err:
            raise Exception(f"Error al actualizar el repositorio: {err}")

    def delete_repo(self, repo_name: str):
        try:
            repo = self.gl.projects.get(id=repo_name)
            repo.delete()
            return True
        except Exception as err:
            raise Exception(f"Error al borrar el repo: {err}")

    def get_project(self, id: str):
        try:
            project = self.gl.projects.get(id=id)
            return project
        except Exception as err:
            raise Exception(f"Error al obtener los proyectos: {err}")

    def clone_repo(
        self,
        projectId: str,
        branchName: str,
        repo_root_dir: str = "./",
        cloning_mode: str = "http",
        user: str = "",
        password: str = "",
    ):
        try:
            project = self.gl.projects.get(id=projectId)
            if not os.path.exists(os.path.join(repo_root_dir, project.name.lower())):
                if cloning_mode == "ssh":
                    # SSH version
                    git.Git(repo_root_dir).clone(project.ssh_url_to_repo)
                elif cloning_mode == "http":
                    # HTTPS version
                    link = project.http_url_to_repo.split("https://")[1]
                    url = f"https://{user}:{password}@{link}"
                    cmd = f"""git clone {url} && cd {project.path}/
                              && git pull origin {branchName}"""
                    subprocess.call(
                        cmd.replace("\n", "").replace("  ", " "), shell=True
                    )
                    time.sleep(5)
                else:
                    raise Exception("Error: no valid cloning mode provided")
            return project
        except Exception as err:
            raise Exception(f"Error al clonar el repositorio: {err}")

    def clone_and_push_repo(
        self, url: str, NewDirectory: str, templateName: str, isJenkins: str
    ):
        try:
            if isJenkins == "True":
                cmd = f"""git clone {url} && cd {NewDirectory}/
                    && git pull origin main
                    && git checkout -b dev"""
                subprocess.call(cmd.replace("\n", "").replace("  ", " "), shell=True)
                cmd = f"cp -r -u {templateName}/. {NewDirectory}/"
                time.sleep(2)
                subprocess.call(cmd, shell=True)
                cmd = f"""cd {NewDirectory}/
                        && git add .
                        && git commit -m 'Init project'
                        && git remote set-url origin {url}
                        && git push origin dev"""
                subprocess.call(cmd.replace("\n", "").replace("  ", " "), shell=True)
            else:
                cmd = f"""git clone {url} && cd {NewDirectory}/
                      && git pull origin main && rm README.md"""
                subprocess.call(cmd.replace("\n", "").replace("  ", " "), shell=True)
                cmd = f"cp -Rf {templateName}/. {NewDirectory}/"
                time.sleep(2)
                subprocess.call(cmd, shell=True)
                cmd = f"""cd {NewDirectory}/ && git add .
                        && git commit -m 'Init project'
                        && git remote set-url origin {url}
                        && git push origin main"""
                subprocess.call(cmd.replace("\n", "").replace("  ", " "), shell=True)
            return True
        except Exception as err:
            raise Exception(f"Error subir archivos: {err}")

    def get_user(self, username: str):
        try:
            user = self.gl.users.list(username=username)[0]
            return user
        except Exception as err:
            raise Exception(f"Error al obtener usuario: {err}")

    def create_access_token(self, id: str, name: str):
        try:
            myTuple = ("Token", name)
            name = "".join(myTuple)
            access_token = self.gl.projects.get(id).access_tokens.create(
                {"name": name, "scopes": ["api"]}
            )
            return access_token.token
        except Exception as err:
            raise Exception(f"Error al crear token: {err}")

    def remove_to_folders(self, nameProject: str, GitProject: str):
        try:
            cmd = f"rm -rf {nameProject} && rm -rf {GitProject}"
            subprocess.call(cmd, shell=True)
            return True
        except Exception as err:
            raise Exception(f"Error al remover la carpeta del repo: {err}")

    def create_commit_and_push(self, project_id: str, branch_name: str):
        try:
            project = self.gl.projects.get(project_id)
            project.commits.create(
                {
                    "branch": branch_name,
                    "commit_message": "Vercel deployment activation",
                    "actions": [
                        {
                            "action": "update",
                            "file_path": "./README.md",
                            "content": "Vercel deployment activation",
                        }
                    ],
                }
            )
            return True
        except Exception as err:
            raise Exception(f"Error al hacer el commit: {err}")
