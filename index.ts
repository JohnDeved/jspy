export default function test (...args: any[]) {
  console.log('hello from ts', ...args)
  return 456
}