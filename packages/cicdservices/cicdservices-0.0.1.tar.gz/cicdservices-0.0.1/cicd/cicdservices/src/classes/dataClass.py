from dataclasses import dataclass, field


@dataclass
class DataClass:
    User: str = field(default="")
    Password: str = field(default="")
    GitUser: str = field(default="")
    GitPassword: str = field(default="")
    NameProject: str = field(default="")
    repoId: str = field(default="")
    projectID: str = field(default="")
    updateProject: str = field(default="")
    Login: bool = field(default=False)

    Framework: str = field(default="")
    BuildOptions: list[str] = field(default_factory=list)
    emails: list[str] = field(default_factory=list)
    Env: dict = field(default_factory=dict)
    EnvAPI: list[str] = field(default_factory=list)
    Group: str = field(default="")
    Link: str = field(default="")
    LinkNewProject: str = field(default="")
    Link_Api_All: str = field(default="https://api.vercel.com/v12/projects/%s?teamId=%s")
    Link_Api_Del: str = field(default="https://api.vercel.com/v12/projects/%s")

    Url: str = field(default="")
    Url_Api: str = field(default="https://api.vercel.com/v12/projects?teamId=%s&s=44")
    CloneUrl: str = field(default="")
    Token: str = field(default="")
    TokenAPI: str = field(default="")
    LinkGit: str = field(default="https://%s:%s@gitlab.com/novateva/%s.git")
    LinkGitClone: str = field(default="https://%s:%s@gitlab.com/%s/%s.git")
    LinkConfig: str = field(default="")

    checkList: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.Url = self.LinkGit % (self.GitUser, self.Token, self.NameProject)
        self.CloneUrl = self.LinkGitClone % (
            self.GitUser,
            self.GitPassword,
            self.GitUser,
            self.NameProject,
        )
