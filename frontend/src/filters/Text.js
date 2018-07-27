var truncatechars = (text, length) => {
  return text.slice(0, length) + (length < text.length ? '...' : '')
}

export {
  truncatechars
}
