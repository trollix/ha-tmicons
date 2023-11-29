  async function getIcon(name) {
    let new_name;
  
    if (!(name in TMICONS_MAP)) {
      // try swapping the '_' for a '-'
      new_name = name.replace(/_/gm, `-`);
      if (!(new_name in TMICONS_MAP)) {
        //console.log(`Icon "${name}" is not available`);
        return '';
      }else{
        console.log(`Aliased "${name}" with "${new_name}"`);
        return {path: TMICONS_MAP[new_name].path};
      }
    }
    return {path: TMICONS_MAP[name].path};
  }
  async function getIconList() {
    return Object.entries(TMICONS_MAP).map(([icon, content]) => ({
      name: icon,
      keywords: content.keywords
    }));
  }
  window.customIcons = window.customIcons || {};
  window.customIcons["tmi"] = { getIcon, getIconList };
  
  window.customIconsets = window.customIconsets || {};
  window.customIconsets["tmi"] = getIcon;
  
  
const CARD_VERSION = '0.2.2';
const CARD_NAME = "HA-TMICONS";
console.info(
  `%c  ${CARD_NAME}  %c  Version ${CARD_VERSION}  `,
    'color: white; font-weight: bold; background: crimson',
    'color: #000; font-weight: bold; background: #ddd',
);
