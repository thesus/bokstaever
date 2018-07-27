var truncatechars = (text, length) => {
  return text.slice(0, length) + (length < text.length ? '...' : '')
}

var chunkify = (text) => {
  return text.split('\n')
}

export {
  truncatechars,
  chunkify
}
