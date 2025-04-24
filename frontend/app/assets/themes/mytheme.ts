import { definePreset } from '@primeuix/themes';
import Aura from '@primeuix/themes/aura';

const MyPreset = definePreset(Aura, {
    semantic: {
      colorScheme: {
        dark: {
          formField: {
            background: '{surface.900}',
          }
        }
      }
    },
});

export default {
    preset: MyPreset,
};
