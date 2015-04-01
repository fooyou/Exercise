#!/usr/bin/python

# Implementation of Charikar simhashes in Python
# See: http://dsrg.mff.cuni.cz/~holub/sw/shash/#a1

class simhash():
    def __init__(self, tokens='', hashbits=64):
        self.hashbits = hashbits
        self.hash = self.simhash(tokens)

    def __str__(self):
        return str(self.hash)

    def __int__(self):
        return int(self.hash)

    def __float__(self):
        return float(self.hash)

    def simhash(self, tokens):
        # Returns a Charikar simhash with appropriate bitlength
        v = [0]*self.hashbits

        for t in [self._string_hash(x) for x in tokens]:
            bitmask = 0
            # print (t)
            for i in range(self.hashbits):
                bitmask = 1 << i
                # print(t,bitmask, t & bitmask)
                if t & bitmask:
                    v[i] += 1 #查看当前bit位是否为1，是的话则将该位+1 
                else:
                    v[i] = v[i] - 1 #否则得话，该位减1

        fingerprint = 0
        for i in range(self.hashbits):
            if v[i] >= 0:
                fingerprint += 1 << i 
        #整个文档的fingerprint为最终各个位大于等于0的位的和
        return fingerprint

    def _string_hash(self, v):
        # A variable-length version of Python's builtin hash
        if v == "":
            return 0
        else:
            x = ord(v[0])<<7
            m = 1000003
            mask = 2**self.hashbits-1
            for c in v:
                x = ((x*m)^ord(c)) & mask
            x ^= len(v)
            if x == -1: 
                x = -2
            return x

    def hamming_distance(self, other_hash):
        x = (self.hash ^ other_hash.hash) & ((1 << self.hashbits) - 1)
        tot = 0
        while x:
            tot += 1
            x &= x-1
        return tot

    def similarity(self, other_hash):
        a = float(self.hash)
        b = float(other_hash)
        if a>b: return b/a
        return a/b

import jieba
if __name__ == '__main__':
    s = '澳大利亚“新快网”12月30日援引澳《悉尼晨锋报》报道，每年公布一次的《澳洲毕业生调查》（Australian Graduate Survey）显示，大学毕业生起薪水平停滞不前，而且获取全职工作的机会更难以触摸。近期毕业的大学生比以往更难找到全职工作，起薪点也不见提高。这份由澳洲毕业生择业机构（Graduate Careers Australia）负责撰写的调查报告显示，全职就业率以及完成学位带来的薪酬优势双双在2014年创新低。32%大学毕业生在获取学位后未能于4个月内找到全职工作，这个比例高于去年同期的29%。“这些数据非常令人担忧。今年的情况比90年代经济萧条时期的还要差。”澳洲智库机构葛拉顿研究所(Grattan Institute) 高等教育项目主管诺顿（Andrew Norton）表示。诺顿指出，大学毕业生全职就业率下滑主要是因为大学录取人数提高，以及雇主在金融危机后不愿意招聘新员工。数据显示，自2009年起取消学位数量上限以来，本科大学生录取率大增23%，即增加录取11万人。在2008年金融危机以前，85%的大学毕业生能在4个月内找到全职工作。但本年的比例已大幅降至68%。据悉，超过10万名近期毕业的大学生参与受访《澳洲毕业生调查》。调查称：“这些数据表明了新一批本科毕业生的就业前景进一步恶化。相比之下，本科毕业生在2009年的就业前景因金融危机而黯淡无光，在2010至2012年期间没有显著变化，但在2013年再次下滑。”目前，制药、医药和矿业工程专业的新毕业生很有可能获取全职工作。然而，社会科学、化学和心理学毕业生最有可能失业或不充分就业。'
    
    print(' '.join(jieba.cut(s)).split())

    hash1 =simhash(' '.join(jieba.cut(s)).split())
    #print("0x%x" % hash1)
    #print ("%s/t0x%x" % (s, hash1))

    s = '古语有云：“国相交，民相亲”。而人类交通和通信的日益便利为“民相交，国相亲”提供了可能。但这并不代表人人皆可做好民间外交。民间外交家应该具备这样的基本素质：既熟悉本国文化，又了解国外文化，有跨文化交流的体验。从这个角度讲，海归天然是民间外交家。留学归国人员是中国故事的调制解调器。相较外国人，他们可以更深入地解码当下中国发生的故事。相较没有留学经验的本土人士，他们可以把这些中国故事用外国人熟悉的符号重新编码。留学归国人员是中国声音的放大器。众所周知，口碑传播是效果最好的传播方式。留学归国人员在海外各界都积累了丰富的人脉，甚至与当地主流文化的意见领袖都建立了良好的个人友谊。通过他们，中国声音得以一传十，十传百。许多怀揣爱国之情的留学归国人员在海外都感觉到外国人对中国不了解，甚至存在偏见。因此，他们有着强烈的意愿去讲好中国故事，传播好中国声音。民间外交的拓展需要海归的更多参与。'
    hash2 = simhash(' '.join(jieba.cut(s)).split())
    #print ("%s/t[simhash = 0x%x]" % (s, hash2))

    print(bin(int(hash1)))
    print(bin(int(hash2)))
    print (hash1.similarity(hash2), "percent similar")
    print (hash1.hamming_distance(hash2), "bits differ out of", hash1.hashbits)
    print('Similarity:', (hash1.hashbits - hash1.hamming_distance(hash2)) / hash1.hashbits)