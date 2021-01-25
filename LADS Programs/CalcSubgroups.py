G = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],
	[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]

subgroups = [[]]

count = 0

for a in range(2):
	for b in range(2):
		for c in range(2):
			for d in range(2):
				for e in range(2):
					for f in range(2):
						for g in range(2):
							for h in range(2):
								for i in range(2):
									for j in range(2):
										for k in range(2):
											for l in range(2):
												for m in range(2):
													for n in range(2):
														for o in range(2):
															for p in range(2):
																if a ==1:
																	subgroups[count].append(G[0])
																if b ==1:
																	subgroups[count].append(G[1])

																if c ==1:
																	subgroups[count].append(G[2])

																if d ==1:
																	subgroups[count].append(G[3])
																											
																if e ==1:
																	subgroups[count].append(G[4])
																if f ==1:
																	subgroups[count].append(G[5])

																if g ==1:
																	subgroups[count].append(G[6])

																if h ==1:
																	subgroups[count].append(G[7])
																												
																if i ==1:
																	subgroups[count].append(G[8])
																if j ==1:
																	subgroups[count].append(G[9])

																if k ==1:
																	subgroups[count].append(G[10])

																if l ==1:
																	subgroups[count].append(G[11])											
																if m ==1:
																	subgroups[count].append(G[12])
																if n ==1:
																	subgroups[count].append(G[13])

																if o ==1:
																	subgroups[count].append(G[14])

																if p ==1:
																	subgroups[count].append(G[15])

																count +=1
																subgroups.append([])

sub_4 = []


for i in subgroups:
	if len(i)==4:
		sub_4.append(i)
		print(i)
print(len(sub_4))