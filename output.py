import _pickle as cPickle


def output_to_pkl(r, pkl_path='./r.pkl'):
    with open(r, 'wb') as pkl_file:
        cPickle.dump(r, pkl_file)


def output_to_txt(r, txt_path='./r.txt'):
    with open(txt_path, "w+", encoding="utf8") as txt_file:
        for i in r:
            txt_file.writelines("\n###" + i[0])
            txt_file.write(i[1].replace('\xa0\xa0\xa0\xa0', '\n'))
