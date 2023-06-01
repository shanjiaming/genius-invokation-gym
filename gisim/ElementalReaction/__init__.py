from .Bloom import *
from .Burning import *
from .Crystallize import *
from .ElectroCharged import *
from .Frozen import *
from .Melt import *
from .Overloaded import *
from .Quicken import *
from .Superconduct import *
from .Swirl import *
from .Vaporize import *
from .base import *

REACTIONLIST = {
    ReactionType.BLOOM: "Bloom",
    ReactionType.BURNING: "Burning",
    ReactionType.CRYSTALLIZE: "Crystallize",
    ReactionType.ELECTROCHARGED: "ElectroCharged",
    ReactionType.FROZEN: "Frozen",
    ReactionType.MELT: "Melt",
    ReactionType.OVERLOADED: "Overloaded",
    ReactionType.QUICKEN: "Quicken",
    ReactionType.SUPERCONDUCT: "Superconduct",
    ReactionType.SWIRL: "Swirl",
    ReactionType.VAPORIZE: "Vaporize",
}


def get_reaction_system(reaction_name: str):
    """通过反应名称查找反应体系"""
    reaction_name = reaction_name.replace(" ", "").replace("'", "")
    reaction_system_class = globals()[reaction_name]
    reaction_system: Reaction = reaction_system_class()
    return reaction_system


def get_reaction_system_by_type(reaction_type: ReactionType):
    """通过反应类型查找反应体系"""
    reaction_name = REACTIONLIST[reaction_type]
    return get_reaction_system(reaction_name)
