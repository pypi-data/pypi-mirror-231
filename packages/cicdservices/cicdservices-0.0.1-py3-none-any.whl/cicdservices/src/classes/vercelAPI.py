import requests

from ..Interfaces.interfaces import BaseInterface
from .dataClass import DataClass


class VercelInterfaceAPI(BaseInterface):
    def __init__(self, data: DataClass):
        self.data = data

    def createVarEnv(self):
        try:
            environment_variables = []
            if len(self.data.Env) > 0:
                for env_var in self.data.Env:
                    env_dict = {
                        "key": env_var["key"],
                        "value": env_var["value"],
                        "target": env_var["target"],
                        "type": env_var["type"],
                    }
                    environment_variables.append(env_dict)

                project_data = {
                    "name": self.data.NameProject,
                    "buildCommand": self.data.BuildOptions[0],
                    "commandForIgnoringBuildStep": "",
                    "devCommand": self.data.BuildOptions[1],
                    "environmentVariables": environment_variables,
                    "framework": self.data.Framework,
                    "gitRepository": {
                        "repo": self.data.BuildOptions[2],
                        "type": self.data.BuildOptions[3],
                    },
                    "installCommand": self.data.BuildOptions[4],
                    "outputDirectory": self.data.BuildOptions[5],
                    "publicSource": True,
                    # "rootDirectory": self.data.BuildOptions[6],
                    "skipGitConnectDuringLink": True,
                }
            else:
                project_data = {
                    "name": self.data.NameProject,
                    "buildCommand": self.data.BuildOptions[0],
                    "commandForIgnoringBuildStep": "",
                    "devCommand": self.data.BuildOptions[1],
                    "framework": self.data.Framework,
                    "gitRepository": {
                        "repo": self.data.BuildOptions[2],
                        "type": self.data.BuildOptions[3],
                    },
                    "installCommand": self.data.BuildOptions[4],
                    "outputDirectory": self.data.BuildOptions[5],
                    "publicSource": True,
                    # "rootDirectory": self.data.BuildOptions[6],
                    "skipGitConnectDuringLink": True,
                }

            return project_data
        except Exception as err:
            print(f"Error in Create Project -> {err}")
            return project_data

    def CreateProject(self):
        try:
            project_data = self.createVarEnv()
            headers = {"Authorization": "Bearer %s" % self.data.TokenAPI}
            if len(project_data) > 0:
                response = requests.post(
                    self.data.Url_Api % self.data.Group, json=project_data, headers=headers
                )

                if response.status_code == 200:
                    response_data = response.json()
                    return response_data
                else:
                    return response.text
        except Exception as err:
            print(f"Error in Create Project -> {err}")
            return False

    def UpdateProject(self):
        try:
            url = self.data.Link_Api_All % (self.data.projectID, self.data.Group)
            headers = {
                "Authorization": "Bearer %s" % self.data.TokenAPI,
                "Content-Type": "application/json",
            }

            data = {
                "buildCommand": self.data.BuildOptions[0],
                "devCommand": self.data.BuildOptions[1],
                "framework": self.data.Framework,
                "installCommand": self.data.BuildOptions[2],
                "name": self.data.updateProject,
                "outputDirectory": self.data.BuildOptions[3]
            }

            response = requests.patch(url, headers=headers, json=data)

            if response.status_code == 200:
                response_data = response.json()
                return response_data
            else:
                raise Exception(response.status_code)
        except Exception as err:
            print(f"Error in Update Project -> {err}")
            return False

    def DeleteProject(self):
        try:
            url = self.data.Link_Api_All % (self.data.projectID, self.data.Group)

            headers = {"Authorization": "Bearer %s" % self.data.TokenAPI}

            response = requests.delete(url, headers=headers)

            if response.status_code == 204:
                return True
            else:
                raise Exception(response.status_code)
        except Exception as err:
            print(f"Error in Delete Project -> {err}")
            return False

    def ReadProject(self):
        try:
            url = self.data.Link_Api_All % (self.data.projectID, self.data.Group)
            headers = {"Authorization": "Bearer %s" % self.data.TokenAPI}

            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                response_data = response.json()
                return response_data
            else:
                raise Exception(response.text)
        except Exception as err:
            print(f"Error in Read Project -> {err}")
            return False

    def Login(self):
        pass
