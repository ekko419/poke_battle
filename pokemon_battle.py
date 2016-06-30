import time
import random

player = {'hp':150}
cpu = {'hp':150}

def tackle(target):
  hitchance = random.randint(1,100)
  if hitchance >= 25:
    damage = random.randint(18,25)
    target -= damage
    print("It did",damage,"damage!\n")
  else:
    print("The attack missed!\n")
  return target

def bodyslam(target):
  hitchance = random.randint(1,100)
  if hitchance >= 35:
    damage = random.randint(14,38)
    target -= damage
    print("It did",damage,"damage!\n")
  else:
    print("The attack missed!\n")
  return target

def heal(target):
  healup = random.randint(18,43)
  target += healup
  if target > 150:
    target = 150
  print("Healed for",healup,"\n")
  return target

print("A battle has begun!\n\n")
while player['hp'] > 0 and cpu['hp'] > 0:
  time.sleep(1)
  print("PLAYER HP:",player['hp'],"\nCPU HP:",cpu['hp'])
  print("\nSelect an attack\n 1: Tackle ---- 2: Bodyslam ---- 3: Heal")
  selection = int(input("What is your selection?: "))
  if selection == 1:
    cpu['hp'] = tackle(cpu['hp'])
  elif selection == 2:
     cpu['hp'] = bodyslam(cpu['hp'])
  elif selection == 3:
    player['hp'] = heal(player['hp'])
  
  if cpu['hp'] > 0:
    print("\nNow it's the computers turn!")
    time.sleep(1)
    cpuselection = random.randint(1,3)
    if cpuselection == 1:
      player['hp'] = tackle(player['hp'])
    elif cpuselection == 2:
      player['hp'] = bodyslam(player['hp'])
    elif cpuselection == 3:
       cpu['hp'] = heal(cpu['hp'])

if player['hp'] <= 0:
  print("\nYou lost! Better luck next time!")
elif cpu['hp'] <= 0:
  print("You won! Congrats!")



