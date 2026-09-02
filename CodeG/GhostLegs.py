"""
Course  : Leetinium
File    : GhostLegs.py
Name    : Cimon

GitHub User: C1M0N
Date: 4/16/25 01:24
"""

p = input()
graph_width_ = int(p.split()[0])
graph_height_ = int(p.split()[1])
graph_ = []
for row_index in range(graph_height_):
    graph_.append(input())
# print(graph_)

# -- |

def ghostLegProphet(graph_width, graph_height, graph):
    result = {}
    result_order = []
    result_index = []
    result_i = 0

    print(graph_width // 3)

    for i in range(0, graph_width // 3 + 1):

        result_index.append(i)

    for char in graph[0]:
        if char != " ":
            result_order.append(char)
            result[char] = None

    print(result_index)
    print(result_order)
    print(result)

    for i in range(1, graph_height):
        if graph[i][0] == "|":
            print ("开始判断第")
            print (i)
            index = 0
            while index < len(result_index):
                if index == 0:
                    print("首")
                    if graph[i][1] == "-":
                        swap_index_pro = result_index[index + 1]
                        result_index[index + 1] = result_index[index]
                        result_index[index] = swap_index_pro
                        index += 2
                    index += 1
                elif index == len(result_index) - 1:
                    print("末")
                    if graph[i][-2] == "-":
                        swap_index_pre = result_index[index - 1]
                        result_index[index - 1] = result_index[index]
                        result_index[index] = swap_index_pre
                        index += 2
                    index += 1
                else:
                    if graph[i][3 * index - 1] == "-":
                        swap_index_pre = result_index[index - 1]
                        result_index[index - 1] = result_index[index]
                        result_index[index] = swap_index_pre
                    elif graph[i][3 * index + 1] == "-":
                        swap_index_pro = result_index[index + 1]
                        result_index[index + 1] = result_index[index]
                        result_index[index] = swap_index_pro
                        index += 2
                    index += 1

                print(result_index)
                print(result_order)
                print(result)

        else:
            for key in result.keys():
                result[key] = graph[graph_height - 1][result_index[result_i]* 3]
                result_i += 1

    # print(result)
    for key,value in result.items():
        print (f"{key}{value}")

ghostLegProphet(graph_width_, graph_height_, graph_)

# region dev
def run_tests():
    import doctest

    doctest.testmod(verbose = True)


def main():
    run_tests()

    pass


if __name__ == "__main__":
    main()
# endregion
