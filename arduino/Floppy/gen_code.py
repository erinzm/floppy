step_pins = range(2, 17, 2)
dir_pins = range(3, 18, 2)
baudrate = 9600

print('void setup() {')
for pin in (step_pins + dir_pins):
    print "pinMode({pin}, OUTPUT);".format(pin=pin)
print('Timer1.initialize(RESOLUTION);')
print('Timer1.attachInterrupt(tick);')
print("Serial.begin({baudrate});".format(baudrate=baudrate))
print('}\n')

print('void resetAll() {')
# stop all notes
for pin in step_pins:
    print("currentPeriod[{pin}] = 0;".format(pin=pin))

print('for(byte s=0;s<80;s++){')
for pin in step_pins:
    print("digitalWriteFast({pin}, HIGH);".format(pin=pin+1))
    print("digitalWriteFast({pin}, HIGH);".format(pin=pin))
    print("digitalWriteFast({pin}, LOW);".format(pin=pin))
print('}')

for pin in step_pins:
    print("currentPosition[{pin}] = 0;".format(pin=pin))
    print("digitalWriteFast({pin}, LOW);".format(pin=pin+1))
    print("currentState[{pin}] = 0;".format(pin=pin+1))

print('}')
