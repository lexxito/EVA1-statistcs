import numpy as np
import matplotlib.pyplot as plt


def make_dict_from_data(path, start_year):
    struct_dict = {}
    f = open(path, "r+")
    research = ""
    for line in f:
        if line.startswith("---"):
            research = line.split("---")[1]
            struct_dict[research] = {}
            struct_dict[research][0] = 0
            for year in range(start_year, 2019):
                struct_dict[research][year] = 0
        if "year" in line:
            year = int(line.split("{")[1].split("}")[0])
            if year < start_year:
                year = 0
            if year in struct_dict[research]:
                struct_dict[research][year] += 1
            else:
                struct_dict[research][year] = 1

    return struct_dict


my_dict = make_dict_from_data("data.txt", 2010)

for res in my_dict:
    x = np.array(range(len(my_dict[res])))
    keylist = my_dict[res].keys()
    keylist.sort()
    additional = 0
    y_array = []
    my_xticks = []
    for key in keylist:
        value = my_dict[res][key] + additional
        my_xticks.append(str(key))
        y_array.append(value)
        additional = value
    plt.xticks(x, my_xticks)
    plt.plot(x, np.array(y_array),linewidth=2, c=np.random.rand(3,1), label=res)
plt.legend(loc="upper left", bbox_to_anchor=[0, 1],
           ncol=2, shadow=True, title="Legend", fancybox=True)
plt.xlabel('year')
plt.ylabel('number of papers')
plt.title('Scientific work trends')
plt.show()
