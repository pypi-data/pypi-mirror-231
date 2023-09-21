import subprocess
import time

import git
from github import Github, GithubException

from ..Interfaces.git import RepoAPI


class GitHubAPI(RepoAPI):
    def __init__(self, token: str):
        self.g = Github(token)

    def search_group(self, group_name: str):
        pass

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
        pass

    def get_statistics(self, repo_name: str, emails: str):
        pass

    def create_access_token(self, id: str, name: str):
        pass

    def remove_to_folders(self, name: str, templateName: str):
        pass

    def clone_repo(self, repo_name: str, user: str, token: str):
        try:
            url = f"https://{user}:{token}@github.com/{user}/{repo_name}.git"
            repo_clone = git.Repo.clone_from(url, repo_name)
            cmd = f"""cd {repo_name} && rm -rf .git"""
            subprocess.call(cmd.replace("\n", "").replace("  ", " "), shell=True)
            return repo_clone
        except GithubException as e:
            raise Exception(f"Error al clonar el repositorio: {e}")

    def create_repo(self, repo_name: str):
        try:
            user = self.g.get_user()
            repo = user.create_repo(repo_name, auto_init=True, private=True)
            return repo
        except GithubException as e:
            raise Exception(f"Error al crear el projecto: {e}")

    def delete_repo(self, name: str):
        try:
            user = self.g.get_user()
            repo = user.get_repo(name)
            repo.delete()
            return True
        except GithubException as e:
            raise Exception(f"Error al borrar el repo: {e}")

    def update_repo(self, repo_name: str, new_name: str):
        try:
            user = self.g.get_user()
            repo = user.get_repo(repo_name)
            if new_name:
                repo.edit(name=new_name)
            return repo
        except GithubException as e:
            raise Exception(f"Error al actualizar el repositorio: {e}")

    def add_users_to_repo(self, name: str, username: str):
        try:
            repo = self.g.get_repo(name)
            repo.add_to_collaborators(username)
            return repo
        except GithubException as e:
            raise Exception(f"Error al agregar usuario al repositorio: {e}")

    def remove_users_from_repo(self, name: str, username: str):
        try:
            user = self.g.get_user()
            repo = user.get_repo(name)
            repo.remove_from_collaborators(username)
            return repo
        except GithubException as e:
            raise Exception(f"Error al eliminar usuario al repositorio: {e}")

    def get_project(self, name: str):
        try:
            user = self.g.get_user()
            repo = user.get_repo(name)
            repo_info = {
                "Nombre del repositorio": repo.name,
                "Descripción del repositorio": repo.description,
                "URL del repositorio": repo.html_url,
                "Propietario del repositorio": repo.owner.login,
                "Lenguaje principal del repositorio": repo.language,
                "Número de estrellas": repo.stargazers_count,
                "Número de horquillas (forks)": repo.forks_count
            }
            return repo_info
        except GithubException as e:
            raise Exception(f"Error al obtener los proyectos: {e}")

    def clone_and_push_repo(
        self, url: str, NewDirectory: str, templateName: str, isJenkins: str
    ):
        try:
            if isJenkins == "True":
                cmd = f"""git clone {url} && cd {NewDirectory}/ 
                    && git pull origin main"""
                subprocess.call(cmd.replace("\n", "").replace("  ", " "), shell=True)
                cmd = f"cp -Rf {templateName}/. {NewDirectory}/"
                subprocess.call(cmd, shell=True)
                time.sleep(2)
                cmd = f"""cd {NewDirectory}/ && git remote set-url origin {url} 
                          && git checkout -b dev 
                          && git add . 
                          && git commit -m 'Init project' 
                          && git push origin dev"""
                print(cmd)
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
        except GithubException as e:
            raise Exception(f"Error subir archivos: {e}")

    def get_user(self, username: str):
        try:
            user = self.g.get_user(username)
            return user
        except GithubException as e:
            raise Exception(f"Error al obtener usuario: {e}")

    def create_commit_and_push(self, project_id: str, branch_name: str):
        try:
            repo = self.g.get_user().get_repo(project_id)
            file_name = "README.md"
            file_content = "Vercel deployment activation"
            archivo = repo.get_contents(file_name, ref=branch_name)

            repo.update_file(
                path=file_name,
                message="Vercel deployment activation",
                content=file_content,
                sha=archivo.sha,
                branch=branch_name,
            )
            return True
        except GithubException as err:
            raise Exception(f"Error al hacer el commit: {err}")
