def can_chain(dominoes):

    if not dominoes:
        return []

    if len(dominoes) == 1:
        if dominoes[0][0] == dominoes[0][1]:
            return dominoes
        return None

    def invert_domino(domino):
        domino_list = list(domino)

        domino_list[0], domino_list[1] = domino_list[1], domino_list[0]

        return tuple(domino_list)

    def can_connect(used_dominoes, candidate):

        last_domino = used_dominoes[-1]
        result = None

        if last_domino[1] == candidate[0]:
            result = (used_dominoes, candidate)

        elif last_domino[1] == candidate[1]:
            result = (used_dominoes, invert_domino(candidate))

        return result

    def build_chain(used_dominoes, unused_dominoes):

        # base case
        if not unused_dominoes:
            if used_dominoes[0][0] == used_dominoes[-1][1]:
                return used_dominoes

        if not used_dominoes:
            used_dominoes.append(unused_dominoes.pop(0))

        for domino in unused_dominoes:
            can_connect_result = can_connect(used_dominoes, domino)

            if can_connect_result:
                updated_used_dominoes = can_connect_result[0] + [can_connect_result[1]]

                updated_unused_dominoes = unused_dominoes.copy()
                updated_unused_dominoes.remove(domino)

                result = build_chain(updated_used_dominoes, updated_unused_dominoes)

                if result:
                    return result

        return None

    return build_chain([], dominoes.copy())
