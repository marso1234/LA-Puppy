from vector import Vector, Valid_mtx
#Helper Functions To Send Message in Discord
def sendExample(command):
  return f'\nCheck `!Vector Example {command}`'

async def VectorSum(message):
  command = message.content.split(' ')
  if len(command) >= 4:
    vector_ls = command[2:]
    base = Valid_mtx(vector_ls[0])
    return_msg = 'Adding\n'+base.get_print()+'\n'
    try:
      for v_string in vector_ls[1:]:
        target = Valid_mtx(v_string)
        return_msg+= 'By\n'+target.get_print()+'\n'
        a = base.sum(target)
        if a[0] == -1:
          await message.channel.send('Invalid Arguments For Vector Sum (matrix1, matrix2, ...)')
          break
        base = a[1]
      return_msg += 'Is Equal To\n'+base.get_print()+'\n'
      await message.channel.send(return_msg)
    except Exception as e:
      print(e)
      await message.channel.send('Invalid Arguments For Vector Sum (matrix1, matrix2, ...)')
  else:
    await message.channel.send('Not Enough Arguments For Vector Sum (matrix1, matrix2, ...)'+sendExample('Sum'))


async def Multiply(message):
  command = message.content.split(' ')
  if len(command) == 4:
    try:
      vector_ls = command[2:]
      base = Valid_mtx(vector_ls[0])
      target = Valid_mtx(vector_ls[1])
      return_msg = 'Multiplying\n'+base.get_print()+'\n'
      return_msg+= 'By\n'+target.get_print()+'\n'
      
      a = base.multiply(target)
      if a[0] == -1:
        await message.channel.send('Invalid Arguments For Vector Multiplication (matrix1, matrix2)')
      else:
        return_msg += 'Is Equal To\n'+a[1].get_print()+'\n'
        await message.channel.send(return_msg)
    except Exception as e:
      print(e)
      await message.channel.send('Invalid Arguments For Vector Multiplication (matrix1, matrix2)')
  else:
    await message.channel.send('Invalid Number Of Arguments Vector Multiplication (matrix1, matrix2)'+sendExample('Multiply'))

async def DotProduct(message):
  command = message.content.split(' ')
  if len(command) == 4:
    try:
      vector_ls = command[2:]
      base = Valid_mtx(vector_ls[0])
      target = Valid_mtx(vector_ls[1])
      return_msg = 'Dot Proudct Of\n'+base.get_print()+'\n'
      return_msg+= 'And\n'+target.get_print()+'\n'
      a = base.dot(target)
      if a[0] == -1:
        await message.channel.send('Invalid Arguments For Dot Product (v1, v2)')
      else:
        return_msg += 'Is Equal To\n'+str(a[1])+'\n'
        await message.channel.send(return_msg)
    except Exception as e:
      print(e)
      await message.channel.send('Invalid Arguments For Dot Product (v1, v2)')
  else:
    await message.channel.send('Invalid Number Of Arguments For Dot Product (v1, v2)!'+sendExample('Dot'))


async def Length(message):
  command = message.content.split(' ')
  if len(command) == 3:
    try:
      vector_ls = command[2:]
      base = Valid_mtx(vector_ls[0])
      return_msg = 'Length Of\n'+base.get_print()+'\n'
      a = base.length()
      if a[0] == -1:
        await message.channel.send('Invalid Arguments For Length')
      else:
        return_msg += 'Is Equal To\n'+str(a[1])+'\n'
        await message.channel.send(return_msg)
    except Exception as e:
      print(e)
      await message.channel.send('Invalid Arguments For Length (v1)')
  else:
    await message.channel.send('Invalid Number Of Arguments For Length! (v1)'+sendExample('Length'))

async def ScalarMultiply(message):
  command = message.content.split(' ')
  if len(command) == 4:
    try:
      vector_ls = command[2:]
      base = Valid_mtx(vector_ls[0])
      return_msg = 'Multiply\n'+base.get_print()+'\n'+'by '+vector_ls[1] + '\n'
      a = base.scalar_multiply(vector_ls[1])
      if a[0] == -1:
        await message.channel.send('Invalid Arguments For Length')
      return_msg += 'Is Equal To\n'+base.get_print()+'\n'
      await message.channel.send(return_msg)
    except Exception as e:
      print(e)
      await message.channel.send('Invalid Arguments For Scalar Product (v1, m)')
  else:
    await message.channel.send('Invalid Number Of Arguments For Scalar Product (v1, m)'+sendExample('Scalar'))


async def Distance(message):
  command = message.content.split(' ')
  if len(command) == 4:
    try:
      vector_ls = command[2:]
      base = Valid_mtx(vector_ls[0])
      target = Valid_mtx(vector_ls[1])
      return_msg = 'Distance Between\n'+base.get_print()+'\n'
      return_msg+= 'And\n'+target.get_print()+'\n'
      a = base.Distance(target)
      if a[0] == -1:
        await message.channel.send('Invalid Arguments For Distance (v1, v2)')
      else:
        return_msg += 'Is Equal To\n'+str(a[1])+'\n'
        await message.channel.send(return_msg)
    except Exception as e:
      print(e)
      await message.channel.send('Invalid Arguments For Distance (v1, v2)')
  else:
    await message.channel.send('Invalid Number Of Arguments For Distance (v1, v2)'+sendExample('Distance'))


async def Determinant(message):
  command = message.content.split(' ')
  if len(command) == 3:
    try:
      vector_ls = command[2:]
      base = Valid_mtx(vector_ls[0])
      isSquare = base.IsSquare()
      if isSquare:
        return_msg = 'Determinant Of\n'+base.get_print()+'\n'
        return_msg+= 'Is Equal To\n'+str(base.Determinant())+'\n'
      else:
        return_msg = 'Please Input A Square Matrix For Determinant'
      await message.channel.send(return_msg)
    except Exception as e:
      print(e)
      await message.channel.send('Invalid Arguments For Determinant (m1)')
  else:
    await message.channel.send('Invalid Number Of Arguments For Determinant (m1)'+sendExample('Determinant'))


async def Echelon(message):
  command = message.content.split(' ')
  if len(command) >= 3:
    try:
      vector_ls = command[2:]
      try:
        is_detailed = vector_ls[1].upper() == 'DETAILED'
      except:
        is_detailed = False
      base = Valid_mtx(vector_ls[0])
      return_msg = 'To Reduce \n'+base.get_print()+'\nTo Echelon Form\n'
      extra_msg  = base.to_echelon()
      if is_detailed:
        return_msg+= extra_msg
      return_msg += 'The Result is \n'+base.get_print()
      await message.channel.send(return_msg)
    except Exception as e:
      print(e)
      await message.channel.send('Invalid Arguments For Echelon (v1)')
  else:
    await message.channel.send('Invalid Number Of Arguments For Echelon (v1)'+sendExample('Echelon'))

async def Inverse(message):
  command = message.content.split(' ')
  if len(command) >= 3:
    try:
      vector_ls = command[2:]
      try:
        is_detailed = vector_ls[1].upper() == 'DETAILED'
      except:
        is_detailed = False
      base = Valid_mtx(vector_ls[0])
      if not base.IsSquare():
        await message.channel.send("Please Input A Square Matrirx To Find Its Inverse")
      if base.Determinant() == 0:
        await message.channel.send("The Determinant Of This Matrix Is 0, Which Shows That The Matrix Is Not Invertible")
        return
      return_msg = 'The Inverse Of \n'+base.get_print()+'\nIs\n'
      extra_msg  = base.Inverse()
      if is_detailed:
        return_msg+= extra_msg
      return_msg += 'The Result is \n'+base.get_print()
      await message.channel.send(return_msg)
    except Exception as e:
      print(e)
      await message.channel.send('Invalid Arguments For Echelon (v1)')
  else:
    await message.channel.send('Invalid Number Of Arguments For Echelon (v1)'+sendExample('Inverse'))