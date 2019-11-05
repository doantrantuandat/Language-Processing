import numpy as np
# Cac nhan tu loai
states = ('khac', 'NN', 'VB')

# Cac tu can xac dinh
observations = ('toi', 'viet', 'baocao')

# bang xac suat chuyen tu loai cho tu dau tien (start)
start_probability = {'khac': 0.3, 'NN': 0.4, 'VB': 0.3}

# bang xac suat chuyen tu loai cho khac, NN, VB
transition_probability = {
   'khac' : {'khac': 0.2, 'NN': 0.2, 'VB': 0.6},
   'NN' : {'khac': 0.4, 'NN': 0.1, 'VB': 0.5},
   'VB' : {'khac': 0.1, 'NN': 0.8, 'VB': 0.1}
   }

# bang xac suat nhan. nhan tu loai
emission_probability = {
   'khac' : {'toi': 0.01, 'viet': 0.02, 'baocao': 0.02},
   'NN' : {'toi': 0.8, 'viet': 0.01, 'baocao': 0.5},
   'VB' : {'toi': 0.19, 'viet': 0.97, 'baocao': 0.48}
   }

# In xac suat viterbi qua cac buoc lam (dang table)
def print_dptable(V, obs):
    s = "    " + " ".join(("%7s" % i) for i in (obs)) + "\n"
    for y in V[0]:
        s += "%.5s: " % y
        s += " ".join("%.7s" % ("%f" % v[y]) for v in V)
        s += "\n"
    print(s)
 
# ham tinh xac suat viterbi
def viterbi(obs, states, start_p, trans_p, emit_p):
    # V la dictionary xac suat viterbi tuong ung cho tung tu "toi", "viet", "baocao"
    # vi du: tu "toi" co xac suat Viterbi {'khac': 0.003, 'NN': 0.3200, 'VB': 0.0569}
    V = [{}] 
    path = {} # duong dan xac dinh tu loai
    # vong lap tinh xac suat cho start
    for y in states: 
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]
    # vong lap tinh xac suat cho cac tu tiep theo
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}
        for y in states:
            (prob, state) = max((V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states)
            V[t][y] = prob
            newpath[y] = path[state] + [y]
        path = newpath
 
    print_dptable(V, obs)
    (prob, state) = max((V[t][y], y) for y in states)
    return (prob, path[state])

def main():
    return viterbi(observations,
                   states,
                   start_probability,
                   transition_probability,
                   emission_probability)
print(main())
