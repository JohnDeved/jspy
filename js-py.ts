import { python } from 'pythonia'
const pythonExit = (python as any).exit as () => void

interface hello_py {
  test: (...args) => Promise<number>
}

const { test } = await python('./py/hello.py') as hello_py
console.log(`got ${await test(', hey')} from python`)
pythonExit()