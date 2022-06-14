async def Example(message):
  command = message.content.split(' ')
  if len(command) >= 3:
    try:
      action = command[2].upper()
      if action == 'SUM':
        await message.channel.send('!Vector Sum 1,2,3:5,6,7 4,0.5,6:7,-10,3')
      elif action == 'MULTIPLY':
        await message.channel.send('!Vector multiply 1,2,3:4,5,6:7,8,9 9,8,7:6,5,4:3,2,1')
      elif action == 'DOT':
        await message.channel.send('!Vector Dot 1,2,3 4,5,6')
      elif action == 'DISTANCE':
        await message.channel.send('!Vector Distance 0.5,12,9 5,7,3')
      elif action == 'LENGTH':
        await message.channel.send('!Vector Length 0.5,12,9')
      elif action == 'SCALAR':
        await message.channel.send('!Vector Scalar 1,2,3:2,4,6:3,6,9 10')
      elif action == 'DET':
        await message.channel.send('!Vector Det 1,2,3,4:4,5,6,4:7,8,9,7:4,3,5,4')
      elif action == 'ECHELON':
        await message.channel.send('!Vector Echelon 1,2,4,4:4,5,4,4:7,8,4,4:4,3,4,4 Detailed')
      elif action == 'INVERSE':
        await message.channel.send('!Vector Inverse 1,4,5:8,3,6:7,6,3')
      else:
        await message.channel.send('Please Input a command to show example\nTo show the command, type !Vector Help')
    except Exception as e:
      print(e)
      await message.channel.send('Unexpected Error To show Example')
  else:
    await message.channel.send('Please Input a command to show example')