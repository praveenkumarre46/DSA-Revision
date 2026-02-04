class FreqStack:

    def __init__(self):
        self.stack=[]
        self.freq={}
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val in self.freq:
            self.freq[val]+=1
        else:
            self.freq[val]=1
    def pop(self) -> int:
        ind=-1
        maxfreq=0
        for i in range(len(self.stack)-1,-1,-1):
            if (self.freq.get(self.stack[i],0)>maxfreq):
                ind=i
                maxfreq=self.freq[self.stack[i]]
        val=self.stack.pop(ind)
        self.freq[val] -= 1
        if self.freq[val] == 0:
            del self.freq[val]
        return val
        