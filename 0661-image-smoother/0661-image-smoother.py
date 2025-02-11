class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        r = len(img)
        c = len(img[0])

        new_img = [[0]*r for _ in range(c)]

        val1 = (img[0][0] + img[0][1] + img[1][0] + img[1][1])
        new_img[0][0] = new_img[0][2] = new_img[2][0] = new_img[2][2] = val1 // 4
        val2 = val1 + img[0][2] + img[1][2]
        new_img[0][1] = new_img[1][0] = new_img[1][2] = new_img[2][1] = val2 // 6
        val3 = val2 + img[2][0] + img[2][1]
        new_img[1][1] = (val3 + img[2][2]) // 9

        return new_img

        