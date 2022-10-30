class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        creator_view_count = defaultdict(int)
        creator_ids_map = defaultdict(list)
        popularity = 0
        for creator, _id, view in zip(creators, ids, views):
            creator_view_count[creator] += view
            creator_ids_map[creator].append((_id, view))
            popularity = max(popularity, creator_view_count[creator])
            
        popular_creators = []
        for creator, view_count in creator_view_count.items():
            if popularity == view_count:
                popular_creators.append(creator)
            
        result = []
        for each in popular_creators:
            temp = creator_ids_map[each]
            temp.sort(key=lambda x: (-x[1], x[0]))
            result.append([each, temp[0][0]])
            
        return result