from my_modules.ninja import Ninja
from my_modules.pet import Pet



ninja1 = Ninja(
    "Jackie",
    "Chan",
    ["kibbles", "bits"],
    5,
    Pet(
        "Mr. Pickles",
        "Guinea Pig",
        ["roll over", "dance"]))


ninja1.feed().walk().bathe()
