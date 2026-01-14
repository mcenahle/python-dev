# 小贝需要翻译的文章
article = "Getting Old Is Easy. Growing Up is Complicated\nWhen you were a child, you wanted to grow up and be able to do everything that age prevents you from doing. You wanted to stay up all night. You dreamt of driving a car, traveling far away with friends, buying whatever you wanted... About all, you longed to do whatever you wanted.\nHowever, as you got older, you became aware of a sad reality. You can't always do what you want. Moreover, being an adult is complicated and even boring. Sometimes, you might even find yourself longing to be a child again. That's how contradictory we human beings are. Furthermore, when you complain, you age a little more every day, forgetting the most important thing: growing up.\nSo, what does growing up really mean? Unlike getting older, it implies you stop simply reacting to what happens to you and act on what happens to you. It involves learning from every experience, big or small, wonderful or tragic. It also means developing a calmer mental focus and understanding that you might not have control over many things, but you have control over yourself.\nThat's right, our society is full of adults who act like children. They're men and women who, despite having matured physically, haven't really grown up as they haven't matured emotionally. They're people that stumble in the face of every adversity, whether big or small. They want the world to respond to their needs and for everything to go the way they want it to go.\nThese people get frustrated quickly. They go from anger to rage, longing for others to adjust to their expectations and desires. It doesn't matter that they're wearing adult costumes, inside they're lost creatures who haven't learned from their experiences because they can't tolerate the fact that life hasn't turned out the way they want.\nInstead of reacting to everything that happens to you, you must integrate self-reflection into each of your experiences. Looking at each event from the serenity of accepting and understanding what's happening to you and employing the appropriate strategies to solve your problems is essential. In fact, growing up means acquiring a more humble and curious approach, as well as being wiser and more hopeful."
# 词汇表，摘录自扇贝单词《高考考纲词汇(2021版)》
wordlist = ['adjust', 'adult', 'approach', 'appropriate', 'aware', 'being', 'complain', 'complicated', 'curious', 'despite', 'essential', 'focus', 'hopeful', 'means', 'moreover', 'reality', 'respond', 'solve', 'tolerate']

# 按行分割英文原文，将结果保存到 paras 列表中
paras = article.split('\n')
# 遍历 paras 列表，每访问到一段内容，将其保存到 para 中
for para in paras:
    # 打印原文并换行
    print(para + '\n')
    # 按空格分割 para，将结果保存到 words 列表中
    words = para.split(' ')
    # 创建列表 new_words，用于保存本段生词
    new_words = []
    # 遍历 words 列表，每访问到一个词，将其保存到 word 中
    for word in words:
        # 从 word 中提取出单词 pure_word
        # 第一步：去除词尾标点符号
        word_without_punctuation = word.strip(",.?!-'")
        # 第二步：转换为小写字母
        pure_word = word_without_punctuation.lower()
        # 如果 pure_word 是生词，则记录下来
        if pure_word in wordlist:
            new_words.append(pure_word)

    # 段落处理完毕，打印本段生词
    # 如果有生词，打印“生词：xxx, xxx, ...”
    if new_words:
        print('生词：' + ', '.join(new_words) + '\n')
        # 否则打印“生词：无”
    else:
        print('生词：无' + '\n')
