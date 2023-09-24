from pydantic import BaseModel, Extra


class DissConfig(BaseModel, extra=Extra.ignore):
    """Plugin Config Here"""

    diss_enabled: bool = True

    diss_global_blacklist: list = []

    diss_global_chance: float = 0.1

    diss_global_cd: float = 5.0
