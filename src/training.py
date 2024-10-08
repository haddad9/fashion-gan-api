import tensorflow as tf

def compile_gan(generator, discriminator):
    discriminator.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    discriminator.trainable = False
    gan_input = tf.keras.Input(shape=(100,))
    generated_image = generator(gan_input)
    gan_output = discriminator(generated_image)
    gan = tf.keras.Model(gan_input, gan_output)
    gan.compile(loss='binary_crossentropy', optimizer='adam')
    return gan

def train_gan(generator, discriminator, gan, processed_data, epochs=1000, batch_size=128):
    for epoch in range(epochs):
        noise = tf.random.normal([batch_size, 100])
        generated_images = generator.predict(noise)
        real_images = processed_data.sample(batch_size)
        labels_real = tf.ones((batch_size, 1))
        labels_fake = tf.zeros((batch_size, 1))

        d_loss_real = discriminator.train_on_batch(real_images, labels_real)
        d_loss_fake = discriminator.train_on_batch(generated_images, labels_fake)
        
        noise = tf.random.normal([batch_size, 100])
        g_loss = gan.train_on_batch(noise, tf.ones((batch_size, 1)))

        if epoch % 100 == 0:
            print(f"Epoch {epoch}, D Loss Real: {d_loss_real}, D Loss Fake: {d_loss_fake}, G Loss: {g_loss}")