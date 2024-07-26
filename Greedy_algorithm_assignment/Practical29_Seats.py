MOD = 10**9 + 7

def minJumps(seats):
	
	position = []

	count = 0

	lenn = len(seats)

	for i in range(lenn):

		if (seats[i] == 'x'):

			position.append(i - count)
			count += 1

	if (count == lenn or count == 0):
		return 0

	med_index = (count - 1) // 2

	med_val = position[med_index]

	ans = 0

	for i in range(len(position)):
		
		ans = (ans % MOD +
			abs(position[i] - med_val)
			% MOD) % MOD

	return ans % MOD

if __name__ == '__main__':
	
	S = "....x..xx...x.."

	print(minJumps(S))
