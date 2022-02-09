import {Dimensions, StyleSheet, View} from 'react-native';
import {Shadow} from 'react-native-shadow-2';
import {AnnotationArea} from '../utils/AnnotationArea';

const windowWidth = Dimensions.get('window').width;
const windowHeight = Dimensions.get('window').height;

function Word() {
  return (
    <View style={styles.main}>
      <Shadow>
        <View style={styles.box}>
          <AnnotationArea />
        </View>
      </Shadow>
    </View>
  );
}

const styles = StyleSheet.create({
  main: {
    flex: 1,
  },
  box: {
    backgroundColor: 'white',
    alignSelf: 'center',
    height: windowHeight / 3.0,
    width: windowWidth / 1.5,
    borderRadius: 35,
    borderWidth: 20,
    borderColor: '#0071ac',
    overflow: 'hidden',
  },
});
export default Word;
