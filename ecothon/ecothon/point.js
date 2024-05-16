return (
    <SafeAreaView style={styles.container}>
      <ScrollView style={styles.scrollView}>
      <View style={styles.banner}>
                    <Image style={styles.miniLogo2} source={require('./assets/logoGreen.png')} />
                    <Text style={styles.point}>Points</Text>
                    <Text style={styles.text2}>Here are all your points. Keep it going for a reward!</Text>
                </View>

                <Text style={styles.largeText}>{this.state.count}</Text>
                <TouchableOpacity onPress={this.increment} style={[styles.box, styles.elevation]}>
                    <Text style={styles.text5}>You brought a reusable straw!</Text>
                    <Text style={styles.text6}>Points: 50</Text>
                    <Text style={styles.text7}>Tap to claim points reward!</Text>
                </TouchableOpacity>

                <TouchableOpacity onPress={this.increment2} style={[styles.box, styles.elevation]}>
                    <Text style={styles.text5}>You chose to use paper bags!</Text>
                    <Text style={styles.text6}>Points: 20</Text>
                    <Text style={styles.text7}>Tap to claim points reward!</Text>
                </TouchableOpacity>

                <TouchableOpacity style={[styles.box, styles.elevation]}>
                    <Text style={styles.text5}>You took the public bus today!</Text>
                    <Text style={styles.text6}>Points: CLAIMED!</Text>
                </TouchableOpacity>
                <TouchableOpacity style={[styles.box, styles.elevation]}>
                    <Text style={styles.text5}>You planted a plant today!</Text>
                    <Text style={styles.text6}>Points: CLAIMED!</Text>
                </TouchableOpacity>

                <TouchableOpacity style={[styles.box, styles.elevation]}>
                    <Text style={styles.text5}>You bought from a sustainable clothing brand!</Text>
                    <Text style={styles.text6}>Points: CLAIMED!</Text>
                </TouchableOpacity>

      </ScrollView>
    </SafeAreaView>
  );
};