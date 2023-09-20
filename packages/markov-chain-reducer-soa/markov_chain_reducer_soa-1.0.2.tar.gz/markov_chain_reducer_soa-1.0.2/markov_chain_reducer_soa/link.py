class Link:
    """
    Содержит информацию о связи между двумя звеньями
    (или одним, если это петля)
    ------------------------------------------------
    Contains information about interconnections between
    two units (or maybe one if it is a loop link)
    """

    def __init__(self, p: float, t: float) -> None:
        """
        Конструктор связи между звеньями
        --------------------------------
        Link constructor between units


        Args:
            p (float): вероятность перехода | probability of the transition
            t (float): временной регламент  | time constraint
        """
        self.p = p
        self.t = t

    def __str__(self) -> str:
        return f"Link(p={self.p}, t={self.t})"
