import os
import uuid
from typing import Optional

import git
from rich import print

from datazone.core.common.config import ConfigReader
from datazone.models.config import Config
from datazone.service_callers.crud import CrudServiceCaller
from datazone.utils.helpers import is_git_repo, initialize_git_repo


def git_push_changes(commit_message: Optional[str] = None) -> None:
    """
    Push changes to the repository. If commit message is not provided, it will be generated automatically as uuid.
    Args:
        commit_message (Optional[str]): Optional commit message
    """
    commit_message = commit_message or str(uuid.uuid4())

    repo = git.Repo()
    origin = repo.remotes.origin

    origin.fetch()
    repo.git.checkout("master")

    repo.index.add("*")
    repo.index.commit(commit_message)
    origin.push("master")
    print("[green]Files have pushed to the repository.[/green]:rocket:")


def deploy(file: Optional[str] = None, commit_message: Optional[str] = None) -> None:
    """
    Deploy project to the repository.
    Args:
        file: path to the custom config file
        commit_message: commit message
    """
    if not is_git_repo():
        config_file = ConfigReader(file)

        if not config_file.is_config_file_exist():
            print("[bold red]Config file does not exist![/bold red]")
            return

        config: Config = config_file.read_config_file()
        project = CrudServiceCaller(service_name="job", entity_name="project").get_entity_with_id(
            entity_id=str(config.project_id),
        )
        for pipeline in config.pipelines:
            pipeline_file = pipeline.path
            if not os.path.exists(pipeline_file):
                print(f"[bold red]Pipeline file {pipeline_file} does not exist![/bold red]")
                return

        repository_name = project.get("repository_name")
        initialize_git_repo(repository_name=repository_name)

    print("[bold green]Deploying...[/bold green]")
    git_push_changes(commit_message)
