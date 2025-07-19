class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans =[]
        for f in folder:
            if not ans:
                ans.append(f)
            else:
                prev = ans[-1]
                if f.startswith(prev) and len(f)>len(prev) and f[len(prev)] == '/':
                    continue
                else:
                    ans.append(f)
        return ans
        