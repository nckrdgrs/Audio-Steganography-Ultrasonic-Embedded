# Use wave package (native to Python) for reading the received audio file
import wave
song = wave.open("song_embedded_complete.wav", mode='rb')
# Convert audio to byte array

frame_bytes = bytearray(list(song.readframes(song.getnframes())))
# print(frame_bytes)

frame_bytes = [frame_bytes[i] for i in range(0,len(frame_bytes),2)]
# print(frame_bytes)

# Extract the LSB of each byte
extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]

print(extracted)
print(len(extracted))
print(extracted[0:0+8])
print(int("".join(map(str,extracted[0:0+8])),2))  #int(str,2)
print(chr(80))

# Convert byte array back to string
string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
# Cut off at the filler characters
decoded = string.split("###")[0]

# Print the extracted text
print("Sucessfully decoded: "+decoded)
song.close()