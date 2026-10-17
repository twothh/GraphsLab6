
import networkx as nx
import matplotlib.pyplot as plt


def main():
    print("Проверка планарности графа")
    print("-" * 35)

    # Ввод количества вершин
    n = int(input("Введите количество вершин: "))

    if n < 1:
        print("Ошибка: граф должен содержать хотя бы одну вершину.")
        return

    G = nx.Graph()
    G.add_nodes_from(range(1, n + 1))

    # Ввод количества рёбер
    m = int(input("Введите количество рёбер: "))

    if m < 0:
        print("Ошибка: количество рёбер не может быть отрицательным.")
        return

    print("Введите рёбра в формате: начало конец")

    for i in range(m):
        u, v = map(
            int,
            input(f"Ребро {i + 1}: ").split()
        )

        if u not in G or v not in G:
            print("Ошибка: вершина не входит в граф.")
            return

        if u == v:
            print("Ошибка: петли в этом задании не поддерживаются.")
            return

        G.add_edge(u, v)

    # Вывод исходного графа
    print("\nВершины графа:", list(G.nodes()))
    print("Рёбра графа:", list(G.edges()))
    print("Количество вершин:", G.number_of_nodes())
    print("Количество рёбер:", G.number_of_edges())

    # Комбинаторная укладка и проверка планарности
    is_planar, embedding = nx.check_planarity(
        G, counterexample=True
    )

    if is_planar:
        print("\nРезультат: граф планарен.")
        print("Комбинаторная укладка успешно построена.")

        # Геометрическая укладка по комбинаторной
        pos = nx.combinatorial_embedding_to_pos(embedding)

        # Отображение графа
        plt.figure(figsize=(9, 7))

        nx.draw_networkx(
            G,
            pos=pos,
            with_labels=True,
            node_color="lightblue",
            node_size=800,
            edge_color="black",
            font_size=12,
            font_weight="bold",
            width=1.5
        )

        plt.title("Геометрическая укладка планарного графа")
        plt.axis("equal")
        plt.axis("off")
        plt.tight_layout()

        # Сохранение рисунка
        plt.savefig("planar_graph.png", dpi=300,
                    bbox_inches="tight")
        print("Рисунок сохранён в файле planar_graph.png")

        plt.show()

    else:
        print("\nРезультат: граф НЕ планарен.")
        print("Найден подграф, свидетельствующий о непланарности:")
        print("Вершины:", list(embedding.nodes()))
        print("Рёбра:", list(embedding.edges()))

        print(
            "\nГеометрическая укладка без пересечений "
            "для данного графа невозможна."
        )


if __name__ == "__main__":
    main()
