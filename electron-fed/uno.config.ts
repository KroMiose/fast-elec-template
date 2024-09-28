// uno.config.ts
import { defineConfig, presetAttributify, presetUno, presetIcons } from 'unocss'
export default defineConfig({
  presets: [
    presetAttributify(),
    presetUno(),
    //自动引入图标库
    presetIcons({
      scale: 1.2,
      warn: true
    })
  ]
})
