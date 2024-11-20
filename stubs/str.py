from itertools import product

def generate_sentences(wordSet, sentence):
    # 将 wordSet 转换为小写，并建立变位词组字典
    wordSet = [word.lower() for word in wordSet]
    anagram_dict = {}
    for word in wordSet:
        key = ''.join(sorted(word)) # 按字母排序作为key
        anagram_dict.setdefault(key, []).append(word)
    
    # 分割句子
    words = sentence.lower().split()
    
    # 对每个单词找到可能的替换项
    replacements = []
    for word in words:
        key = ''.join(sorted(word))
        replacements.append(anagram_dict.get(key, [word]))
    
    # 使用笛卡尔积生成所有可能组合
    all_sentences = [' '.join(combination) for combination in product(*replacements)]
    
    return all_sentences

# 测试输入
wordSet = ["listen", "silent", "it", "is"]
sentence = "listen it is silent"

result = generate_sentences(wordSet, sentence)
print(f"生成的句子数量: {len(result)}")
print("生成的句子:")
for sent in result:
    print(sent)
