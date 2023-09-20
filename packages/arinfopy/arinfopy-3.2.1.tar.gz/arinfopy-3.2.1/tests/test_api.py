import arinfopy as apy

# test = apy.adsobin("/Users/beps/Simularia/Progetti/BIG-IoT/data/wanda/" +
#                    "conc/2017-12-17/conc_elise.bin_n1_d1_t1")
test = apy.adsobin("./tests/surfpro3.bin")
rec3 = test.getRecord3(deadline=1)
immai = rec3['immai']
jmmai = rec3['jmmai']
rec5 = test.getRecord5(deadline=1)
print("List of 3D variables: {}".format(rec5['nomvar3d']))
print("List of 2D variables: {}".format(rec5['nomvar2d']))

# for n in range(1000):
rec7 = test.getRecord7(deadline=1)

tempk = test.getDataset("TEMPK")

print(f"Tempk size: {tempk.size}")
print(f"Templ shape: {tempk.shape}")

deadlines = test.getDeadlines()
for nd in range(len(test)):
    print(f"Deadline {deadlines[nd]}; max tempk = {tempk[nd,:,:,:].max()}")


rel = test.getDataset("REL")
print(f"rel shape: {rel.shape}")

# slice = test.getSlice(variable='PHI')
# for n in range(1000):
#     slice = test.getSlice(variable='M001S001')
#     slice = test.getSlice(variable='M002S002', slice=2)
# slice = test.getSlice(variable='M003S003', slice=2, deadline=53)
# slice = test.getSlice(variable='REL')
# slice = test.getSlice(variable='CONCAN ', deadline=2)
# slice = test.getSlice(variable='RELa')
# slice = test.getSlice(variable='U', slice=2, deadline=1)
print("done")
