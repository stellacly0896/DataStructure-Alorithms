# python3

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i])

    def SiftDown(self,i):
        minIndex = i
        left = 2*i
        right = 2* i + 1

        if left <= len(self.nodes) - 1:
            if self.nodes[left][1] <self.nodes[minIndex][1]:
                minIndex = left
            elif self.nodes[left][1] == self.nodes[minIndex][1] and self.nodes[left][0] < self.nodes[minIndex][0]:
                minIndex = left

        if right <= len(self.nodes) - 1:
            if self.nodes[right][1] <self.nodes[minIndex][1]:
                minIndex = right
            elif self.nodes[right][1] == self.nodes[minIndex][1] and self.nodes[right][0] < self.nodes[minIndex][0]:
                minIndex = right

        if i != minIndex:
            self.nodes[i],self.nodes[minIndex] = self.nodes[minIndex],self.nodes[i]
            self.SiftDown(minIndex)

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        self.nodes = [None] + [[x,0] for x in range(self.num_workers)]

        for i in range(len(self.jobs)):
            self.assigned_workers[i] = self.nodes[1][0]
            self.start_times[i] = self.nodes[1][1]
            self.nodes[1][1] += self.jobs[i]
            self.SiftDown(1)


    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

