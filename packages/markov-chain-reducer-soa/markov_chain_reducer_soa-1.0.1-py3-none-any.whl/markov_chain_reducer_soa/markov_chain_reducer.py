from .link import Link


class MarkovChainReducer:
    """
    Решает задачи сокращения цепей Маркова для предмета
    SOA
    ---------------------------------------------------
    Intends to solve Markov's chains reduction problems
    during the SOA lessons
    """

    @staticmethod
    def round_link(link: Link, ndigits: int = 3) -> float:
        """
        Округлить значения в связи до ndigits знаков после запятой
        -----------------------------------------------------------
        Round values in the link untill ndigits digits after period
        """
        return Link(
            p=round(link.p, ndigits=ndigits),
            t=round(link.t, ndigits=ndigits),
        )

    @staticmethod
    def reduce_unit_links(left: Link, right: Link) -> Link:
        """
        Убрать прямую связь между звеньями
        ----------------------------------
        Remove forward link between units

               p1,2   p2,3                   p1,3'
        E.G: (1) -> (2) -> (3 fin)  ==>   (1) -> (3 fin)
               t1,2   t2,3        reduce     t1,3'

        Formulas:
                    for p =>  p1,3' = p1,2 * p2,3
                    for t =>  t1,3' = t1,2 + t2,3

        Args:
            left (Link):  связь между 1 и 2 звеньями | link between 1 and 2 units
            right (Link): связь между 2 и 3 звеньями | link between 2 and 3 units

        Returns:
            Link: результирующая связь между 1 и 3 звеньями |
                  resulting link between 1 and 2 units
        """
        return Link(
            p=left.p * right.p,
            t=left.t + right.t,
        )

    @staticmethod
    def reduce_loop_link(loop_link: Link, right: Link) -> Link:
        """
        Убрать петлю
        ------------
        Reduce loop

                p2,2 t2,3                   p2,3'
        E.G: (2 loop) -> (3 fin)  ==>    (2) -> (3 fin)
                t2,2 t2,3       reduce      t2,3'

        Formulas:
                    for p =>  p2,3' = p2,3 / (1 - p2,2)
                    for t =>  t2,3' = t2,3 + ((t2,2 * p2,2) / (1-p2,2))

        Args:
            loop_link (Link): связь-петля 2,2            | loop link 2,2
            right (Link):     связь между 2 и 3 звеньями | link between 2 and 3 units

        Returns:
            Link: результирующая связь между 2 и 3 звеньями |
                  resulting link between 2 and 3 units
        """
        return Link(
            p=right.p / (1 - loop_link.p),
            t=right.t + ((loop_link.t * loop_link.p) / (1 - loop_link.p)),
        )

    @staticmethod
    def reduce_parallel_links(upper: Link, lower: Link) -> Link:
        """
        Убрать параллельную связь
        -------------------------
        Reduce parallel link

               p2,3;t2,3
                 ->                  p2,3''
        E.G: (2)    (3 fin)  ==>  (2) -> (3 fin)
                 ->         reduce   t2,3''
               p2,3';t2,3'

        Formulas:
                    for p =>  p2,3'' = p2,3 + p2,3'
                    for t =>  t2,3'' = (t2,3 * p2,3 + t2,3' * p2,3') / (p2,3 + p2,3')

        Args:
            upper (Link): верхняя связь | upper link
            lower (Link): нижняя свзяь  | lower link

        Returns:
            Link: результирующая связь между 2 и 3 звеньями
        """
        return Link(
            p=upper.p + lower.p,
            t=(upper.t * upper.p + lower.t * lower.p) / (upper.p + lower.p),
        )

    @staticmethod
    def reduce_forward_backward_loop(forward: Link, backward: Link) -> Link:
        """
        Убрать петлю между звеньями
        -----------------------------
        Reduce loop between two units

        (Аналогичный метод методу MarkovChainReducer.reduce_unit_links)

             p3,2;t3,2
                <-              p2,2
        E.G: (2)   (3)  =>   (2 loop)
                ->    reduce    t2,2
             p2,3;t2,3

        Formulas:
                    for p =>  p2,2 = p2,3 * p3,2
                    for t =>  t2,2 = t2,3 + t3,2

        Args:
            forward  (Link): прямая связь между 2 и 3 звеньями |
                             forward link between 2 and 3 units
            backward (Link): обратная связь между 2 и 3 звеньями |
                             backward link between 2 and 3 units

        Returns:
            Link: связь-петля 2,2 | loop link 2,2
        """
        return MarkovChainReducer.reduce_unit_links(forward, backward)

    @staticmethod
    def reduce_unit_with_fb_loop_link(
        left: Link, forward: Link, backward: Link
    ) -> (Link, Link):
        """
        Убрать петлю между звеньями и превратить в петлю саму на себя
        ---------------------------------
        Reduce loop between two units and turn it into a loop on itself

                    p3,2;t3,2
                p1,2    <-                   p1,3'  p3,3
        E.G: (1) -> (2)    (3) ->...  =>    (1) -> (3 loop) ->...
                t1,2    ->          reduce    t1,3'  t3,3
                    p2,3;t2,3

        Formulas:
                    for p1,3' =>  p1,3' = p1,2 * p2,3
                    for t1,3' =>  t1,3' = t1,2 + t2,3
                    for p3,3  =>  p3,3  = p3,2 * p2,3
                    for t3,3  =>  t3,3  = t3,2 + t2,3

        Args:
            left     (Link): левое звено цепи |
                             left unit of the chain
            forward  (Link): прямая связь между 2 и 3 звеньями |
                             forward link between 2 and 3 units
            backward (Link): обратная связь между 2 и 3 звеньями |
                             backward link between 2 and 3 units

        Returns:
            Link1: связь между 1 и 3 звеном | link between 1 and 2 units
            Link2: связь-петля 3,3          | loop link 3,3
        """
        # TODO: дополнить документацию функции
        return (
            MarkovChainReducer.reduce_unit_links(left, forward),
            MarkovChainReducer.reduce_unit_links(forward, backward),
        )
