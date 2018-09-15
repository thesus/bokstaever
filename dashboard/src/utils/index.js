const propExists = (obj, path) => {
  return !!path.split('.').reduce((obj, prop) => {
    return obj && obj[prop] ? obj[prop] : undefined
  }, obj)
}

export {
  propExists
}
