# 小贝需要翻译的文章
article = "Getting Old Is Easy. Growing Up is Complicated\nWhen you were a child, you wanted to grow up and be able to do everything that age prevents you from doing. You wanted to stay up all night. You dreamt of driving a car, traveling far away with friends, buying whatever you wanted... About all, you longed to do whatever you wanted.\nHowever, as you got older, you became aware of a sad reality. You can't always do what you want. Moreover, being an adult is complicated and even boring. Sometimes, you might even find yourself longing to be a child again. That's how contradictory we human beings are. Furthermore, when you complain, you age a little more every day, forgetting the most important thing: growing up.\nSo, what does growing up really mean? Unlike getting older, it implies you stop simply reacting to what happens to you and act on what happens to you. It involves learning from every experience, big or small, wonderful or tragic. It also means developing a calmer mental focus and understanding that you might not have control over many things, but you have control over yourself.\nThat's right, our society is full of adults who act like children. They're men and women who, despite having matured physically, haven't really grown up as they haven't matured emotionally. They're people that stumble in the face of every adversity, whether big or small. They want the world to respond to their needs and for everything to go the way they want it to go.\nThese people get frustrated quickly. They go from anger to rage, longing for others to adjust to their expectations and desires. It doesn't matter that they're wearing adult costumes, inside they're lost creatures who haven't learned from their experiences because they can't tolerate the fact that life hasn't turned out the way they want.\nInstead of reacting to everything that happens to you, you must integrate self-reflection into each of your experiences. Looking at each event from the serenity of accepting and understanding what's happening to you and employing the appropriate strategies to solve your problems is essential. In fact, growing up means acquiring a more humble and curious approach, as well as being wiser and more hopeful."

# 按「\n」分割 article，将结果保存到 paras 列表中
paras = article.split('\n')

# 遍历列表 paras

# 遍历列表 paras
for para in paras:
    # 将自然段切分成若干词语
    words = para.split(' ')
    # 打印本自然段单词数量
    print(len(words))
# 将自然段切分成若干词语
# 打印本自然段单词数量
