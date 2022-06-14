import discord
import os
import MessageManager
from Example import Example
from keep_alive import keep_alive
client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  '''
  if message.author == client.user:
    return
  '''
  isCommand = message.content.split(' ')[0].upper()=='!VECTOR'
  if isCommand:
    if len(message.content)>1024:
      return
    command = message.content.split(' ')
    action = command[1].upper()
    if action == 'HELP':
      await message.channel.send('Welcome To LA- Puppy, Here are the commands:\nTo Represent a Matrix, just seperate rows by \' , \' and columns by \' : \'\n\n-----**Matrix**-----\n*Sum* - Finding Matrix Sum\n*Multiply* - Multiply Two Matrixes\n*Scalar* - Multiply Matrix By A Scalar Value\n*Det* - Find Determinant of a square Matrix\n*Echelon* - Reduce a matrix to echelon form, using argument \'detailed\' for steps\n*Inverse* - Find Inverse of the Matrix\n\n-----**Vector**-----\n*Dot* - Calculating Dot Product\n*Distance* - Find Distance Between Two Vector\n*Length* - Find Length Of Vector\n\n-----**General**-----\n*Example* - Show Example of a command\n*Clear* - Delete Recent 10 Messages') 
    elif action == 'SUM':
      await MessageManager.VectorSum(message)
    elif action =='CLEAR':
      await message.channel.purge(limit=11,bulk=False)
    elif action == 'MULTIPLY':
      await MessageManager.Multiply(message)
    elif action == 'DOT':
      await MessageManager.DotProduct(message)
    elif action == 'LENGTH':
      await MessageManager.Length(message)
    elif action == 'SCALAR':
      await MessageManager.ScalarMultiply(message)
    elif action == 'DISTANCE':
      await MessageManager.Distance(message)
    elif action == 'EXAMPLE':
      await Example(message)
    elif action == 'DET':
      await MessageManager.Determinant(message)
    elif action == 'ECHELON':
      await MessageManager.Echelon(message)
    elif action == 'INVERSE':
      await MessageManager.Inverse(message)


keep_alive()
client.run(os.getenv("TOKEN"))