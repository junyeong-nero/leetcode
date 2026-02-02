from collections import Counter


class Solution:
    def minimumTeachings(
        self, n: int, languages: List[List[int]], friendships: List[List[int]]
    ) -> int:
        # 1. 언어 데이터를 set으로 변환 (교집합 확인을 위해)
        lang_sets = [set(l) for l in languages]

        # 2. 소통이 안 되는 친구 쌍에 속한 사람들 찾기
        unconnected_people = set()
        for u, v in friendships:
            # u, v는 1-indexed이므로 index 조정
            if not (lang_sets[u - 1] & lang_sets[v - 1]):
                unconnected_people.add(u)
                unconnected_people.add(v)

        if not unconnected_people:
            return 0

        # 3. 소통 안 되는 사람들 중에서 각 언어를 이미 알고 있는 사람 수 세기
        lang_counts = Counter()
        for p in unconnected_people:
            for l in lang_sets[p - 1]:
                lang_counts[l] += 1

        # 4. (전체 대상 인원) - (특정 언어를 이미 아는 사람의 최대 수)
        # 즉, 가장 많이 겹치는 언어를 선택하고 나머지를 가르치는 게 이득
        max_already_knows = max(lang_counts.values()) if lang_counts else 0

        return len(unconnected_people) - max_already_knows


# class Solution:
#     def minimumTeachings(
#         self, n: int, languages: List[List[int]], friendships: List[List[int]]
#     ) -> int:

#         counter = Counter()
#         people = set()

#         graph = defaultdict(list)
#         for u, v in friendships:
#             graph[u].append(v)
#             graph[v].append(u)

#         def comm(node):
#             counter = Counter()
#             cur = set(languages[node - 1])
#             candidates = set()

#             for neigh in graph[node]:
#                 if cur & set(languages[neigh - 1]):
#                     continue
#                 candidates.add(neigh)
#                 counter += Counter(languages[neigh - 1])

#             if not candidates:
#                 return 0

#             candidates.add(node)
#             counter += Counter(languages[node - 1])

#             lang, freq = counter.most_common()[0]
#             res = 0

#             for neigh in candidates:
#                 if lang in languages[neigh - 1]:
#                     continue
#                 languages[neigh - 1].append(lang)
#                 res += 1

#             return res

#         res = 0
#         nodes = sorted(graph.keys(), key=lambda x: len(graph[x]), reverse=True)
#         for node in nodes:
#             print(node, languages)
#             res += comm(node)

#         return res

# for u, v in friendships:
#     inter = set(languages[u - 1]) & set(languages[v - 1])
#     if inter:
#         continue

#     counter += Counter(languages[u - 1])
#     counter += Counter(languages[v - 1])
#     people.add(u)
#     people.add(v)

# if not people:
#     return 0

# lang, freq = counter.most_common()[0]
# print(lang, freq)

# res = 0
# for person in people:
#     if lang in languages[person - 1]:
#         continue
#     res += 1

# # 중복되는 index 제거.
# return res

