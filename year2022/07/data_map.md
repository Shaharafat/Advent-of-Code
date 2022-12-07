- /
- ls 
    dir a
    file b
    file c
    dir d



root={
  'a':{
    type: 'dir'
    parent:'/'
  }
  'b': 1233423
  'c': 34234
  'd': {
    type:'dir',
    parent: '/'
  }

}

a = {
  total=231,
  
}

root['a']={
  'e':{
    type:'dir'
  }
  'f':2343
  'g': 23423
  'hdf':43243
  parent: 'a'
}

root['a']['e'] = {

}
