raw_corpus = ["I'd like an apple.", "An apple a day keeps the doctor away.", "Never compare an apple to an orange", "I prefer scikit-learn to orange."]

'''
    tf = number of times that the term appears in the document/
        number of terms that that the document d has
'''

word_set = set()
corpus = []
for doc in raw_corpus:
    doc = preprocess(doc)
    words = doc.split(' ')
    word_set = word_set.union(set(words))
    corpus.append(doc)

n_docs = len(corpus)
n_words = len(word_set)

df_tf = pd.DataFrame(np.zeros((n_docs, n_words)), columns=list(word_set))

for i in range(n_docs):
    words = corpus[i].split(' ')
    for w in words:
        df_tf[w][i] = df_tf[w][i] + (1/len(words))

'''
    idf = log(Number of documents/Number of documents that contains the term t)
'''

idf = {}
for w in word_set:
    k=0
    for i in range(n_docs):
        doc = corpus[i]
        if w in doc.split(' '):
            k += 1
    idf[w] = np.log10(n_docs/k)


df_tf_idf = df_tf.copy()

for w in word_set:
    for i in range(n_docs):
        df_tf_idf[w][i] = df_tf[w][i] * idf[w]

'''
    idf = log(number of documents/number of document containing term t)
'''

mat = np.dot(df_tf_idf, df_tf_idf.T)

print(np.argmax(mat[0, 1:]) + 2)
