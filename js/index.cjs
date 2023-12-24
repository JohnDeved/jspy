module.exports = function test (...args) {
  console.log('hello from js', ...args)
  return 123
}