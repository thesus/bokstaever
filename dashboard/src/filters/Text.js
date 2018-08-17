const truncatechars = (text, length) => {
  return text.slice(0, length) + (length < text.length ? '...' : '')
}

const chunkify = (text) => {
  return text.split('\n')
}

const pluralize = (count, word) => {
  return count > 1 ? word + 's' : word
}

export {
  truncatechars,
  chunkify,
  pluralize
}
