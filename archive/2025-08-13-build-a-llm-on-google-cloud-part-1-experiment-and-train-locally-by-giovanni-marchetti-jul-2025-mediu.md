---
date: '2025-08-13'
description: 'Giovanni Marchetti''s article provides a detailed tutorial on building
  a large language model (LLM) using Keras and Google Cloud. It covers the full pipeline:
  local training, scaling with GPU/TPU, fine-tuning, and potential enhancements. Key
  innovations include implementing Grouped Query Attention (GQA), Rotary Positional
  Embeddings (RoPE), and SwiGLU activations, which enhance efficiency and performance.
  The model leverages TensorFlow''s data processing pipeline for efficient batch operations
  and supports sharding across accelerators for scalability. The practical guide is
  aimed at users interested in deploying LLMs on cloud infrastructure with modern
  ML techniques.'
link: https://medium.com/@gmarchetti/build-a-llm-on-google-cloud-d7a49c4d4786
tags:
- LLM
- Google Cloud
- TensorFlow
- Vertex AI
- Keras
title: 'Build a LLM on Google Cloud. Part 1: Experiment and train locally. ◆ by Giovanni
  Marchetti ◆ Jul, 2025 ◆ Medium'
---

[Sitemap](https://medium.com/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd7a49c4d4786&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40gmarchetti%2Fbuild-a-llm-on-google-cloud-d7a49c4d4786&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40gmarchetti%2Fbuild-a-llm-on-google-cloud-d7a49c4d4786&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# Build a LLM on Google Cloud

## Part 1: Experiment and train locally.

[![Giovanni Marchetti](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*FGWcSoowYLpVC1Dj)](https://medium.com/@gmarchetti?source=post_page---byline--d7a49c4d4786---------------------------------------)

[Giovanni Marchetti](https://medium.com/@gmarchetti?source=post_page---byline--d7a49c4d4786---------------------------------------)

Follow

12 min read

·

Jul 17, 2025

2

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dd7a49c4d4786&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40gmarchetti%2Fbuild-a-llm-on-google-cloud-d7a49c4d4786&source=---header_actions--d7a49c4d4786---------------------post_audio_button------------------)

Share

In this series of articles, we discuss how to write a modern, large (-ish) language model with Keras and train it on Google Cloud.

The objective is not to create a state-of-the art LLM, rather to explain how Google Cloud services can help you do just that.

We’ll divide the task in 4 parts:

- Part 1 (this article): Build the model, experiment and train locally.
- Part 2: Scale the model and train it on a GPU or TPU Cluster.
- Part 3: Fine-Tune the model and serve it.
- Part 4: Further enhancements (e.g. mixture-of-experts)

Let’s start with exploring and experimenting using [Vertex AI Colab Enterprise](https://cloud.google.com/vertex-ai/docs/colab/create-console-quickstart). We’ll build out the model in the notebook environment and run a few experiments.

## 1.1 Data Pre-Processing

First we need a dataset. We can start with a relatively small one such as “ [Simplebooks](https://arxiv.org/abs/1911.12391)”, which contains about 92M word-level tokens.

The data consists of several text files, which we can ingest into a Tensorflow dataset for pre-processing. For instance, we want to make sure that the training text is meaningfully long for the task at hand, so we set a `MIN_STRING_LEN ` parameter (e.g. 256 characters). In reality you’ll probably want longer paragraphs than that, but bear with us for this initial experiment.

```
keras.utils.get_file(
    origin="https://dldata-public.s3.us-east-2.amazonaws.com/simplebooks.zip",
    extract=True,
    cache_subdir=BASE_DIR+"/data/",
)
raw_train_tf = (
    tf_data.TextLineDataset(dir + "/data/simplebooks-92-raw/train.txt")
    .filter(lambda x: tf_strings.length(x) > MIN_STRING_LEN)
)

# Load simplebooks-92 validation set and filter out short lines.
raw_val_tf = (
    tf_data.TextLineDataset(dir + "simplebooks-92-raw/valid.txt")
    .filter(lambda x: tf_strings.length(x) > MIN_STRING_LEN)
)
```

The dataset is now composed of tensors containing strings. You can print one out.

```
for element in raw_val_tf.take(1):
    print(element)
tf.Tensor(b'"I am glad of it," said a woolly Lamb on Wheels, who stood on the floor, just under the edge of the toy counter. She was rather too large to be up among the smaller toys. "Yes, I am glad of it," went on the Lamb. "I have kept still all day, and now I have something to tell you all, my friends."', shape=(), dtype=string)
```

We must tokenize it, i.e. split it into atomic units of meaning (tokens) and provide a numerical representation of it for further processing. For that, we need a vocabulary.

```
# Train tokenizer vocabulary
vocab = keras_hub.tokenizers.compute_word_piece_vocabulary(
    raw_train_tf,
    vocabulary_size=VOCAB_SIZE,
    lowercase=True,
    strip_accents=True,
    reserved_tokens=["[PAD]", "[CLS]", "[SEP]", "[UNK]", "[MASK]", "[BOS]", "[EOS]"],
)
```

The vocabulary size of the original GPT model was about 50,000 words. The simple books dataset contains about 98,000, many of which have very low frequency (i.e. appear fewer than 10 times). For this exercise, we keep 50048. We also reserve tokens to indicate beginning and end of sentence ( `[BOS], [EOS]`) and other useful symbols. The computation of a vocabulary can take quite a long time, so one is often provided with the training dataset. In any case, we want to save it for future use.

```
import pickle
with open('/content/simplebooks_vocab.pkl', 'wb') as f:
    pickle.dump(vocab, f)
```

We can use the word piece tokenization method provided by Keras.

```
tokenizer = keras_hub.tokenizers.WordPieceTokenizer(
    vocabulary=vocab,
    sequence_length=SEQ_LEN,
    lowercase=True,
 strip_accents=True
)
```

Note that we must provide a `sequence_length` parameter (e.g. 1024). Most models require a fixed-size input sequence. If the input is longer, it will be truncated; if shorter, padded. The context length of our model will dictate how much of the input sequence can be processed in one pass. Ideally, the former will be a multiple of the latter.

Transformer models generate one token at a time, so the input data is our sequence and the output the same sequence shifted by one. To create them, we use the StartEndPacker utility, which prepends a BOS token and appends a EOS to the sentence.

```
# packer adds a start token and end token
start_packer = keras_hub.layers.StartEndPacker(
    sequence_length=SEQ_LEN,
    start_value=tokenizer.token_to_id("[BOS]"),
    end_value=tokenizer.token_to_id("[EOS]"),
)
def preprocess(inputs):
    outputs = tokenizer(inputs)
    features = start_packer(outputs)
    labels = outputs
    return features, labels
# Tokenize and split into train and label sequences.
train_ds = (raw_train_tf.map(preprocess, num_parallel_calls=tf_data.AUTOTUNE)
            .shuffle(1024, seed=SEED)
            .batch(BATCH_SIZE, drop_remainder=True)
            .prefetch(tf_data.AUTOTUNE)
)
val_ds = (raw_val_tf.map(preprocess, num_parallel_calls=tf_data.AUTOTUNE)
          .batch(BATCH_SIZE, drop_remainder=True)
          .prefetch(tf_data.AUTOTUNE)
)
```

Our data processing pipeline also includes batching and pre-fetching to accelerate processing. An element will be a tensor of size `(batch, sequence_length)`.

```
for element in train_ds.take(1):
    print(element)
(<tf.Tensor: shape=(256, 512), dtype=int32, numpy=
array([[   5,   92, 5756, ...,    0,    0,    6],\
       [   5,  699,   18, ...,    0,    0,    6],\
       [   5,    8,   50, ...,    0,    0,    6],\
       ...,\
       [   5,  204,  161, ...,    0,    0,    6],\
       [   5,    8,  355, ...,    0,    0,    6],\
       [   5,    8,  355, ...,    0,    0,    6]], dtype=int32)>, <tf.Tensor: shape=(256, 512), dtype=int32, numpy=
array([[  92, 5756, 9821, ...,    0,    0,    0],\
       [ 699,   18,   76, ...,    0,    0,    0],\
       [   8,   50,  407, ...,    0,    0,    0],\
       ...,\
       [ 204,  161,   42, ...,    0,    0,    0],\
       [   8,  355,   18, ...,    0,    0,    0],\
       [   8,  355,   18, ...,    0,    0,    0]], dtype=int32)>)
```

## 1.2 Model Definition

Keras provides pre-built Transformer Encoder and Decoder layers. However, those do not implement advanced features such as [grouped query attention](https://arxiv.org/abs/2305.13245), [SwiGLU](https://arxiv.org/pdf/2002.05202) activation or [rotary embeddings](https://arxiv.org/abs/2104.09864). We can build a decoder-only transformer by using Keras Hub component layers to include those.

![](https://miro.medium.com/v2/1*zxR0k3vVkfVJr2DmGdnvng.png)

Transformer Architecture

## 1.2.1 GQA and RoPE

Grouped query attention (GQA) modifies the standard multi-head attention (MHA) mechanisms by creating groups of query heads that share the same set of keys and values. The approach improves inference times while suffering a minimal decrease in accuracy compared to MHA (see the original paper for measurements).

![](https://miro.medium.com/v2/1*IKn-HNZPRSF226YqCO8S5g.png)

Grouped Query Attention

Rotary Positional Embeddings (RoPE) encode position with a rotation matrix, thus maintain relative distance between words in a sequence. They are also efficient to compute and cache.

Keras Hub provides a GQA layer and RoPE, but they are not combined. In the RoFormer [paper](https://arxiv.org/abs/2104.09864), the rotary transformation is applied to queries and keys directly, not to the input tokens embeddings. We amend GQA accordingly.

![](https://miro.medium.com/v2/1*L6GSHE4R0DiG3Rzm-m5JDg.png)

Rotary Positional Embeddings on Query and Key

```
@keras.saving.register_keras_serializable()
class GQAwithRoPE(Layer):
    """Grouped Query Attention layer.

    ... SNIPPET ONLY - FULL CODE PROVIDED IN GITHUB ...

    """

    def __init__(
        self,
        head_dim,
        num_query_heads,
        num_key_value_heads,
        dropout=0.0,
        use_bias=True,
        flash_attention=None,
        kernel_initializer="glorot_uniform",
        bias_initializer="zeros",
        kernel_regularizer=None,
        bias_regularizer=None,
        activity_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None,
        seed=None,
        use_rope=True,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.supports_masking = True
        self.head_dim = head_dim
        self.num_query_heads = num_query_heads
        self.num_key_value_heads = num_key_value_heads
        if num_query_heads % num_key_value_heads != 0:
            raise ValueError(
                "`num_query_heads` must be divisible by `num_key_value_heads`."
            )
        self.num_repeats = num_query_heads // num_key_value_heads
        self.dropout = dropout
        self.use_bias = use_bias
        self._flash_attention = flash_attention or is_flash_attention_enabled()
        self.kernel_initializer = initializers.get(kernel_initializer)
        self.bias_initializer = initializers.get(bias_initializer)
        self.kernel_regularizer = regularizers.get(kernel_regularizer)
        self.bias_regularizer = regularizers.get(bias_regularizer)
        self.activity_regularizer = regularizers.get(activity_regularizer)
        self.kernel_constraint = constraints.get(kernel_constraint)
        self.bias_constraint = constraints.get(bias_constraint)
        self.seed = seed
        self.use_rope = use_rope

        self._inverse_sqrt_head_dim = 1.0 / math.sqrt(float(self.head_dim))
        self._return_attention_scores = False

        # Check for flash attention constraints
        if self._flash_attention and self.dropout > 0.0:
            raise ValueError(
                "Dropout is not supported when flash attention is enabled. "
                "Please set dropout to 0.0 to use flash attention."
            )

    def build(
        self,
        query_shape,
        value_shape,
        key_shape=None,
    ):
        # Einsum variables:
        # b = batch size
        # q = query length
        # k = key/value length
        # m = model dim
        # u = num query heads
        # v = num key/value heads
        # h = head dim
        key_shape = value_shape if key_shape is None else key_shape
        self.feature_dim = query_shape[-1]
        self._query_dense = EinsumDense(
            "bqm,muh->bquh",
            output_shape=(None, self.num_query_heads, self.head_dim),
            bias_axes="uh" if self.use_bias else None,
            name="query",
            **self._get_common_kwargs_for_sublayer(),
        )
        self._query_dense.build(query_shape)

        self._key_dense = EinsumDense(
            "bkm,mvh->bkvh",
            output_shape=(None, self.num_key_value_heads, self.head_dim),
            bias_axes="vh" if self.use_bias else None,
            name="key",
            **self._get_common_kwargs_for_sublayer(),
        )
        self._key_dense.build(key_shape)

        self._value_dense = EinsumDense(
            "bkm,mvh->bkvh",
            output_shape=(None, self.num_key_value_heads, self.head_dim),
            bias_axes="vh" if self.use_bias else None,
            name="value",
            **self._get_common_kwargs_for_sublayer(),
        )
        self._value_dense.build(value_shape)

        self._softmax = Softmax(axis=-1, dtype=self.dtype_policy)
        self._dropout_layer = Dropout(
            rate=self.dropout, dtype=self.dtype_policy, seed=self.seed
        )

        self._dot_product_equation = "bquh,bkuh->buqk"
        self._combine_equation = "buqk,bkuh->bquh"

        self._output_dense = EinsumDense(
            "bquh,uhm->bqm",
            output_shape=(None, self.feature_dim),
            bias_axes="m" if self.use_bias else None,
            name="attention_output",
            **self._get_common_kwargs_for_sublayer(),
        )
        self._output_dense.build(
            (None, None, self.num_query_heads, self.head_dim)
        )

        ############################
        self._rope=RotaryEmbedding()
        ############################

        self.built = True

  # ... SNIPPET ONLY ... #

    def call(
        self,
        query,
        value,
        key=None,
        query_mask=None,
        value_mask=None,
        key_mask=None,
        attention_mask=None,
        return_attention_scores=False,
        training=None,
        use_causal_mask=False,
    ):
        self._return_attention_scores = return_attention_scores
        if key is None:
            key = value

        attention_mask = self._compute_attention_mask(
            query,
            value,
            query_mask=query_mask,
            value_mask=value_mask,
            key_mask=key_mask,
            attention_mask=attention_mask,
            use_causal_mask=use_causal_mask,
        )

        query = self._query_dense(query)
        key = self._key_dense(key)
        value = self._value_dense(value)

        ###########################
        if self.use_rope:
          query = self._rope(query)
          key = self._rope(key)
        ###########################

        key = ops.repeat(
            key, self.num_repeats, axis=2
        )  # (batch_dim, source_seq_len, query_heads, head_dim)
        value = ops.repeat(
            value, self.num_repeats, axis=2
        )  # (batch_dim, source_seq_len, query_heads, head_dim)

        output, scores = self._compute_attention(
            query,
            key,
            value,
            attention_mask=attention_mask,
            training=training,
        )

        output = self._output_dense(
            output
        )  # (batch_dim, target_seq_len, feature_dim)

        if return_attention_scores:
            return output, scores
        return output
 # ... REST OF GQA CODE FOLLOWS ... #
```

## 1.2.2 Feed-Forward Block with SwiGLU

The [SwiGLU](https://arxiv.org/pdf/2002.05202) activation function has been shown to improve the performance of transformer models in several tasks. We amend the feed-forward block in the transformer structure to implement the formulation introduced in the original paper:

## Get Giovanni Marchetti’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

FFNSwiGLU(x, W, V, W2) = (Swish1(xW) ⊗ xV )W2

```
@keras.saving.register_keras_serializable()
class FFNSwiGLU(Layer):
    def __init__(self, intermediate_dim, output_dim, **kwargs):
        super(FFNSwiGLU, self).__init__(**kwargs)
        self.intermediate_dim = intermediate_dim
        self.output_dim = output_dim

    def build(self, input_shape):
        last_dim = input_shape[-1]
        self.gate = Dense(self.intermediate_dim,  use_bias=False, kernel_initializer="glorot_uniform",
                activation="silu", name="swiglu_gate",)
        self.linear = Dense(self.intermediate_dim, use_bias=False, kernel_initializer="glorot_uniform",
                name="swiglu_linear",  )
        self.multiply=Multiply(name="swiglu_multiply")
        self.linearw2 = Dense(self.output_dim, use_bias=False, kernel_initializer="glorot_uniform", name="swiglu_out")

    def call(self, inputs):
        gated = self.gate(inputs)
        linear_out=self.linear(inputs)
        product=self.multiply([gated,linear_out])
        linear_w2=self.linearw2(product)
        return linear_w2 #product

    def get_config(self):
        config = super(FFNSwiGLU, self).get_config()
        config.update({'intermediate_dim': self.intermediate_dim})
        config.update({'output_dim': self.output_dim})
        return config
```

## 1.2.3 Transformer Decoder Block

Now we use the updated attention and feed-forward SwiGLU layers, along with RMS Normalization, to build a decoder block.

```
@keras.saving.register_keras_serializable()
class TransformerBlock(Layer):
    def __init__(self, num_heads, num_kv_heads, embed_dim, ff_dim, dropout_rate=0.0, **kwargs):
        super(TransformerBlock, self).__init__(**kwargs)
        self.num_heads = num_heads
        self.num_kv_heads=num_kv_heads
        self.embed_dim = embed_dim
        self.ff_dim = ff_dim
        self.dropout_rate = dropout_rate

        self.attn = GQAwithRoPE(
            num_query_heads=num_heads,
            num_key_value_heads=num_kv_heads,
            head_dim=embed_dim // num_heads,
            use_rope=True,
            use_bias=False,
            dropout=self.dropout_rate,
            flash_attention=None,
            seed=SEED,
            name="attn",
        )

        self.dropout_1 = Dropout(self.dropout_rate, seed=SEED)
        self.ln_1 = RMSNormalization()
        self.ffn_1 = FFNSwiGLU(self.ff_dim, self.embed_dim, name="ffnswiglu")
        self.dropout_2 = Dropout(self.dropout_rate, seed=SEED)
        self.ln_2 = RMSNormalization()

    def call(self, inputs):
      input_shape = keras.ops.shape(inputs)
      batch_size = input_shape[0]
      seq_len = input_shape[1]
      inputs_n=self.ln_1(inputs)
      attention_output = self.attn(
          query= inputs_n,
          #key= inputs_n,
          value= inputs_n, #quirk of implementation value is required, key is not and assumed = value
          use_causal_mask=True
      )
      attention_output = self.dropout_1(attention_output)
      out1 = self.ln_2(inputs + attention_output)

      ffn_1 = self.ffn_1(out1)
      ffn_output = self.dropout_2(ffn_1)
      return (out1 + ffn_output)

    def get_config(self):
      config = super().get_config()
      config.update(
          {
              "num_kv_heads": self.num_kv_heads,
              "embed_dim": self.embed_dim,
              "num_heads": self.num_heads,
              "ff_dim": self.ff_dim,
              "dropout_rate": self.dropout_rate,
          }
      )
      return config

    def compute_output_shape(self, input_shape):
        # Assumes input_shape is [batch_size, sequence_length, hidden_size]
        batch_size = input_shape[0]
        sequence_length = input_shape[1]
        hidden_size = input_shape[2]
        return [batch_size, sequence_length, hidden_size]
```

## 1.2.4 Sharding

The size of the model is mainly dictated by embedding size, number of transformer layers to be stacked, and size of each transformer block. The Keras model.summary() call will provide a count of the number of parameters and their default memory occupation in float32 format. We can enable mixed precision training using the bfloat16 format instead to save memory.

```
keras.mixed_precision.set_global_policy("mixed_bfloat16")
```

Even so, the summary() call does not take into account the optimizer state representation and the data batches to be stored in the accelerator memory during training. A useful rule of thumb is to assume that total memory occupation will be 3 to 4 times that of the mere parameters.

We may need to shard the weight matrices across accelerators to fit the model onto the available hardware. A detailed discussion of sharding is beyond the scope of this article, but you can find a more in-depth explanation in the Keras3 [documentation](https://keras.io/guides/distribution/). Suffice to say that we can implement a pseudo-FSDP (Fully Sharded, Data Parallel) strategy by using the ModelParallel call on a device mesh representing the accelerators where both data and model weights are distributed across the same axis.

```
device_mesh=keras.distribution.DeviceMesh(
    shape=(
        #DATA_PARALLEL,
        MODEL_PARALLEL,),
    axis_names=[\
        #"data",\
        "model"],
    devices=gpus
)
layout_map=keras.distribution.LayoutMap(device_mesh)

layout_map["embedding/embeddings"] = (None, "model")
# Partitioning (regex) for attention layer weights
layout_map["transformer_block.*attn.*(query|key|value).*kernel"] = (None, "model", None)
layout_map["transformer_block.*attention_output.*kernel"] = (None, None, "model")
layout_map["transformer_block.*swiglu_gate.*kernel"] = ("model", None)
layout_map["transformer_block.*swiglu_linear.*kernel"] = ("model", None)
layout_map["transformer_block.*ffnlinear.*kernel"] = (None, "model")
#layout_map["output/kernel"] = ( None, "model")

##Hybrid DP/MP
model_parallel = keras.distribution.ModelParallel(layout_map=layout_map, batch_dim_name="model")
keras.distribution.set_distribution(model_parallel)
```

It is important to define the mesh before the model is actually built, as the distribution strategy is applied at compilation time.

## 1.2.5 Stack the blocks to build the LLM

The LLM consists of an embedding layer, followed by a stack of transformer decoder blocks and closed by a dense linear output layer that performs a classification. Effectively, it returns the probability distribution (or more accurately the logit distribution, as we want to save ourselves the cost of a softmax operation) of the next token being one of those in the vocabulary. We can build it as follows.

```
## From Llama
decay_steps = 1.2E6
initial_learning_rate = 3e-5
alpha=0.1
warmup_steps = 2000
target_learning_rate = 3e-4
learning_rate = keras.optimizers.schedules.CosineDecay(
    initial_learning_rate,
    decay_steps,
    warmup_target=target_learning_rate,
    warmup_steps=warmup_steps,
    alpha=alpha
)
optimizer=keras.optimizers.AdamW(learning_rate=learning_rate,
                                weight_decay=0.1,
                                beta_1=0.9,
                                beta_2=0.95,
                                epsilon=1e-5,
                                )

## Model definition
inputs = keras.layers.Input(shape=(None,), dtype="int32")

x=layers.Embedding(input_dim=VOCAB_SIZE, output_dim=EMBEDDING_DIM,)(inputs)

for i in range(NUM_BLOCKS):

  # Create a new TransformerBlock instance in each iteration
  x = TransformerBlock(
      N_HEADS, N_KV_HEADS, EMBEDDING_DIM, FEED_FORWARD_DIM,
      dropout_rate=0.1, # does not apply to Attention so fast attention can be used
      name=f"transformer_block_{i}",
  )(x)

x=RMSNormalization()(x)

output = Dense(VOCAB_SIZE,
              use_bias=False,
              #activation="softmax" #we'll use the logits
              #dtype="float32",
              kernel_initializer="glorot_uniform",
              name="output"
              )(x)

gpt = keras.Model(inputs=inputs, outputs=[output])
gpt.compile(optimizer=optimizer,
            loss=[losses.SparseCategoricalCrossentropy(from_logits=True)],
            metrics=[keras_hub.metrics.Perplexity(from_logits=True, mask_token_id=0)],
            jit_compile=True # Enable/Disable JIT compilation
           )
```

## 1.3 Train the model

With all the parts now in place, we can proceed to train the model as any other Keras-based multi-class classification.

Depending on the size of the model and dataset, the training may take hours or days, so we want to define a few callbacks that will allow us to resume computation if errors or failures happen.

In particular, we want to take advantage of the [backup](https://keras.io/api/callbacks/backup_and_restore/) and restore built-in callback and of the model [checkpoints](https://keras.io/api/callbacks/model_checkpoint/). The former is intended to recover training from interruptions, the latter to save whole models that can be reloaded later.

```
checkpoint = keras.callbacks.ModelCheckpoint(
    filepath=f"{STAGING_BUCKET}/checkpoints/{MODEL_NAME}.keras",
    monitor='val_loss',
    mode='min',
    save_best_only=True,
    save_freq="epoch",
    verbose=1)

backupandrestore=keras.callbacks.BackupAndRestore(
    backup_dir=f"{STAGING_BUCKET}/backupandrestore/{MODEL_NAME}", save_freq=10000, double_checkpoint=False, delete_checkpoint=True
)

earlystop=keras.callbacks.EarlyStopping(
    monitor="val_loss",
    min_delta=0,
    patience=5,
    verbose=1,
    mode="min",
    baseline=None,
    restore_best_weights=True,
    start_from_epoch=0,
)

tensorboard=keras.callbacks.TensorBoard(
    log_dir=f"{STAGING_BUCKET}/logs/{MODEL_NAME}",
    histogram_freq=1,
    write_graph=True,
    write_images=False,
    write_steps_per_second=True,
    update_freq=1000, #"epoch",
    profile_batch=1000,
    embeddings_freq=2000,
    embeddings_metadata=None,
)

terminateonnan=keras.callbacks.TerminateOnNaN()

callbacks=[checkpoint,\
           earlystop, tensorboard,\
           backupandrestore,\
           terminateonnan]

try:
    history=gpt.fit(train_ds,
                validation_data=val_ds,
                epochs=EPOCHS,
                callbacks=callbacks,
                verbose=1)
    # save only from worker 0
    if jax.process_index()==0 and len(history.history) > 1000:
        gpt.save(f"{STAGING_BUCKET}/models/{MODEL_NAME}.keras")
    exit(0)
except Exception as e:
    print (e)
    exit(1)
else:
    exit(0)
```

The tensorboard callback will allow us to monitor the progress of our training from another notebook, or visualize it after the fact from the current one.

```
%tensorboard --logdir <gs://STAGING_BUCKET}/logs/MODEL_NAME>
```

If everything goes according to plan, you will be able to see some nicely decreasing plots of loss and perplexity metrics.

![](https://miro.medium.com/v2/1*aK3aet6xQP8jpa9SBoS5eA.png)

Loss and Perplexity

_Hint:_ When perplexity hits 20 or lower, the generated text may start making sense… A 100M-parameter model on the simplebooks dataset (overkill, but just to test things out…) may do that in about 12 hours on 4 x A100–40 GPUs. Your mileage may vary.

## 1.4 Sampling & Generation

The pre-trained model per se just generates a logit distribution. To convert it to a probability distribution, we divide the logits by a _temperature_ value, then we pass the results to a softmax function. A temperature lower than 1 has the effect of sharpening the distribution, a temperature higher than one will instead flatten it.

![](https://miro.medium.com/v2/1*xsNR1k7uZ-2n4EO01jpsFw.png)

Effects of Temperature

To generate text, we must decide which next token to pick out of the distribution. Keras offers several samplers for that purpose. The most obvious one uses a greedy strategy, i.e. it always picks the most probable. This leads to more predictable, if repeating, output.

## 1.4.1 TopK sampling

Alternatively, we select only the top k most-likely logits, re-compute the softmax and then sample according to the resulting probability. This effectively removes the tail of the distribution and makes the generated text less likely to go off-topic, while affording some variety. The original GPT models used TopK for that reason.

```
def next(prompt, cache, index):
    logits = gpt(prompt)[:, index - 1, :]
    # Ignore hidden states for now
    hidden_states = None
    return logits, hidden_states, cache
sampler = keras_hub.samplers.TopKSampler(k=5, temperature=1.2)
output_tokens = sampler(
    next=next,
    prompt=prompt_tokens,
    index=1,
)
txt = tokenizer.detokenize(output_tokens)
print(f"Top-K search generated text: \n{txt}\n")

Top-K search generated text:
['[BOS] " i think it is very well that we should have a good time at the hotel , " the captain said , " if it had been a very pleasant one . the hotel is very large , but i think it will be better for us to go there . there is a good deal more room there . i am very glad i have had the pleasure of seeing this house , " he went on . [EOS]']
```

## 1.4.2 TopP sampling

TopP finds the smallest set of tokens whose output probability sums to a greater number than P, then picks one among those according to their respective re-weighted probability. One can think of it as a “dynamic TopK”, although a k parameter is still used to cut off the tail of the distribution empirically. The resulting text often sounds more fluent than that produced by TopK only.

```
sampler = keras_hub.samplers.TopPSampler(p=0.9, k=10, temperature=1.0)
output_tokens = sampler(
    next=next,
    prompt=prompt_tokens,
    index=1,
)
txt = tokenizer.detokenize(output_tokens)
print(f"Top-P search generated text: \n{txt}\n")
Top-P search generated text:
['[BOS] " we are all here ! " she exclaimed , " and we are going to take a train that will take us to - - to - morrow to see the city . there are a lot of people in that city , " she said as she came up the steps . " i don \' t know whether there \' s a real person in the world - - a man who does not know the city from , but who has been here ever since ? " [EOS] ']
```

**Note**: The code mentioned in this article will be provided in github. Stay tuned for part 2.

[AI](https://medium.com/tag/ai?source=post_page-----d7a49c4d4786---------------------------------------)

[Llm](https://medium.com/tag/llm?source=post_page-----d7a49c4d4786---------------------------------------)

[Gcp](https://medium.com/tag/gcp?source=post_page-----d7a49c4d4786---------------------------------------)

[Vertex AI](https://medium.com/tag/vertex-ai?source=post_page-----d7a49c4d4786---------------------------------------)

[![Giovanni Marchetti](https://miro.medium.com/v2/resize:fill:96:96/0*FGWcSoowYLpVC1Dj)](https://medium.com/@gmarchetti?source=post_page---post_author_info--d7a49c4d4786---------------------------------------)

[![Giovanni Marchetti](https://miro.medium.com/v2/resize:fill:128:128/0*FGWcSoowYLpVC1Dj)](https://medium.com/@gmarchetti?source=post_page---post_author_info--d7a49c4d4786---------------------------------------)

Follow

[**Written by Giovanni Marchetti**](https://medium.com/@gmarchetti?source=post_page---post_author_info--d7a49c4d4786---------------------------------------)

[57 followers](https://medium.com/@gmarchetti/followers?source=post_page---post_author_info--d7a49c4d4786---------------------------------------)

· [74 following](https://medium.com/@gmarchetti/following?source=post_page---post_author_info--d7a49c4d4786---------------------------------------)

Giovanni is a machine learning specialist engineer at Google. His interests include artificial intelligence and high performance computing.

Follow

## No responses yet

![](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)

Write a response

[What are your thoughts?](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40gmarchetti%2Fbuild-a-llm-on-google-cloud-d7a49c4d4786&source=---post_responses--d7a49c4d4786---------------------respond_sidebar------------------)

Cancel

Respond

## More from Giovanni Marchetti

![Unlock Sharepoint with Google Gemini and Llamaindex](https://miro.medium.com/v2/resize:fit:679/1*xTSRneHa1UKjus0fG7LYaw.png)

[![Giovanni Marchetti](https://miro.medium.com/v2/resize:fill:20:20/0*FGWcSoowYLpVC1Dj)](https://medium.com/@gmarchetti?source=post_page---author_recirc--d7a49c4d4786----0---------------------1a0e3fae_9c25_47ca_b403_d88507ebdfc7--------------)

[Giovanni Marchetti](https://medium.com/@gmarchetti?source=post_page---author_recirc--d7a49c4d4786----0---------------------1a0e3fae_9c25_47ca_b403_d88507ebdfc7--------------)

[**Unlock Sharepoint with Google Gemini and Llamaindex**\\
\\
**Microsoft Sharepoint has been around for a number of years. It is the default collaboration tool for many Office users, who share their…**](https://medium.com/@gmarchetti/unlock-sharepoint-with-google-gemini-and-llamaindex-bab54f77ab90?source=post_page---author_recirc--d7a49c4d4786----0---------------------1a0e3fae_9c25_47ca_b403_d88507ebdfc7--------------)

Dec 27, 2023

[A clap icon5\\
\\
A response icon1](https://medium.com/@gmarchetti/unlock-sharepoint-with-google-gemini-and-llamaindex-bab54f77ab90?source=post_page---author_recirc--d7a49c4d4786----0---------------------1a0e3fae_9c25_47ca_b403_d88507ebdfc7--------------)

![Linear Programming for Inventory Optimization](https://miro.medium.com/v2/resize:fit:679/1*-vYS5QfJQBvDBzRGNtTExQ.png)

[![Giovanni Marchetti](https://miro.medium.com/v2/resize:fill:20:20/0*FGWcSoowYLpVC1Dj)](https://medium.com/@gmarchetti?source=post_page---author_recirc--d7a49c4d4786----1---------------------1a0e3fae_9c25_47ca_b403_d88507ebdfc7--------------)

[Giovanni Marchetti](https://medium.com/@gmarchetti?source=post_page---author_recirc--d7a49c4d4786----1---------------------1a0e3fae_9c25_47ca_b403_d88507ebdfc7--------------)

[**Linear Programming for Inventory Optimization**\\
\\
**Our solution guide, SKU optimization for consumer brands, notes that linear programming is often used for assortment and inventory…**](https://medium.com/@gmarchetti/linear-programming-for-inventory-optimization-64aa674a13cc?source=post_page---author_recirc--d7a49c4d4786----1---------------------1a0e3fae_9c25_47ca_b403_d88507ebdfc7--------------)

Dec 7, 2018

[A clap icon6](https://medium.com/@gmarchetti/linear-programming-for-inventory-optimization-64aa674a13cc?source=post_page---author_recirc--d7a49c4d4786----1---------------------1a0e3fae_9c25_47ca_b403_d88507ebdfc7--------------)

![PINNS with Colab Enterprise](https://miro.medium.com/v2/resize:fit:679/1*RhHrQ-71b5Q-BSZIrFE6UQ.png)

[![Giovanni Marchetti](https://miro.medium.com/v2/resize:fill:20:20/0*FGWcSoowYLpVC1Dj)](https://medium.com/@gmarchetti?source=post_page---author_recirc--d7a49c4d4786----2---------------------1a0e3fae_9c25_47ca_b403_d88507ebdfc7--------------)

[Giovanni Marchetti](https://medium.com/@gmarchetti?source=post_page---author_recirc--d7a49c4d4786----2---------------------1a0e3fae_9c25_47ca_b403_d88507ebdfc7--------------)

[**PINNS with Colab Enterprise**\\
\\
**on Vertex AI**](https://medium.com/@gmarchetti/pinns-with-colab-enterprise-d5a1e16572a4?source=post_page---author_recirc--d7a49c4d4786----2---------------------1a0e3fae_9c25_47ca_b403_d88507ebdfc7--------------)

Apr 15, 2024

[A clap icon6](https://medium.com/@gmarchetti/pinns-with-colab-enterprise-d5a1e16572a4?source=post_page---author_recirc--d7a49c4d4786----2---------------------1a0e3fae_9c25_47ca_b403_d88507ebdfc7--------------)

![Recommendations with neural networks](https://miro.medium.com/v2/resize:fit:679/1*SjPxdeoahra38ZtrZhEFsw.png)

[![Giovanni Marchetti](https://miro.medium.com/v2/resize:fill:20:20/0*FGWcSoowYLpVC1Dj)](https://medium.com/@gmarchetti?source=post_page---author_recirc--d7a49c4d4786----3---------------------1a0e3fae_9c25_47ca_b403_d88507ebdfc7--------------)

[Giovanni Marchetti](https://medium.com/@gmarchetti?source=post_page---author_recirc--d7a49c4d4786----3---------------------1a0e3fae_9c25_47ca_b403_d88507ebdfc7--------------)

[**Recommendations with neural networks**\\
\\
**Giovanni Marchetti**](https://medium.com/@gmarchetti/recommendations-with-neural-networks-ad25ea9b6380?source=post_page---author_recirc--d7a49c4d4786----3---------------------1a0e3fae_9c25_47ca_b403_d88507ebdfc7--------------)

Jan 28, 2019

[A clap icon1](https://medium.com/@gmarchetti/recommendations-with-neural-networks-ad25ea9b6380?source=post_page---author_recirc--d7a49c4d4786----3---------------------1a0e3fae_9c25_47ca_b403_d88507ebdfc7--------------)

[See all from Giovanni Marchetti](https://medium.com/@gmarchetti?source=post_page---author_recirc--d7a49c4d4786---------------------------------------)

## Recommended from Medium

![Leave Agentic AI Frameworks And Build Agents From Scratch](https://miro.medium.com/v2/resize:fit:679/1*BYXnNu2kjtLN9ZEQ9XtxvQ.png)

[![AIGuys](https://miro.medium.com/v2/resize:fill:20:20/1*Ga9k_bhbMPfyhDP9_zSIyQ.png)](https://medium.com/aiguys?source=post_page---read_next_recirc--d7a49c4d4786----0---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

In

[AIGuys](https://medium.com/aiguys?source=post_page---read_next_recirc--d7a49c4d4786----0---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

[Vishal Rajput](https://medium.com/@vishal-ai?source=post_page---read_next_recirc--d7a49c4d4786----0---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

[**Leave Agentic AI Frameworks And Build Agents From Scratch**\\
\\
**I’ll be honest with you, I hate most agent-based AI workflows; they are simply unusable in the real world at scale. Despite the…**](https://medium.com/aiguys/leave-agentic-ai-frameworks-and-build-agents-from-scratch-0a45d1656513?source=post_page---read_next_recirc--d7a49c4d4786----0---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

Aug 6

[A clap icon720\\
\\
A response icon26](https://medium.com/aiguys/leave-agentic-ai-frameworks-and-build-agents-from-scratch-0a45d1656513?source=post_page---read_next_recirc--d7a49c4d4786----0---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

![Building the Rickbot Multi-Personality Agentic Application using Gemini CLI, Google…](https://miro.medium.com/v2/resize:fit:679/1*5ZEwP-QSM-sRAIH1fTSlBQ.png)

[![Google Cloud - Community](https://miro.medium.com/v2/resize:fill:20:20/1*FUjLiCANvATKeaJEeg20Rw.png)](https://medium.com/google-cloud?source=post_page---read_next_recirc--d7a49c4d4786----1---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

In

[Google Cloud - Community](https://medium.com/google-cloud?source=post_page---read_next_recirc--d7a49c4d4786----1---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

[Dazbo (Darren Lester)](https://medium.com/@derailed.dash?source=post_page---read_next_recirc--d7a49c4d4786----1---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

[**Building the Rickbot Multi-Personality Agentic Application using Gemini CLI, Google…**\\
\\
**Looking to build agentic solutions with the Google ADK? From scratch or migrating? Use Agent-Starter-Pack and Gemini CLI to accelerate!**](https://medium.com/google-cloud/building-the-rickbot-multi-personality-agentic-application-using-gemini-cli-google-a48aed4bef24?source=post_page---read_next_recirc--d7a49c4d4786----1---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

5d ago

[A clap icon281](https://medium.com/google-cloud/building-the-rickbot-multi-personality-agentic-application-using-gemini-cli-google-a48aed4bef24?source=post_page---read_next_recirc--d7a49c4d4786----1---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

![He Was a Senior Developer, Until We Read His Pull Request](https://miro.medium.com/v2/resize:fit:679/0*CY7pC1JFluXIyWo4.jpg)

[![ThreadSafe Diaries](https://miro.medium.com/v2/resize:fill:20:20/1*VKCStgoerjQ4wL0shVGTrw.png)](https://medium.com/@ThreadSafeDiaries?source=post_page---read_next_recirc--d7a49c4d4786----0---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

[ThreadSafe Diaries](https://medium.com/@ThreadSafeDiaries?source=post_page---read_next_recirc--d7a49c4d4786----0---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

[**He Was a Senior Developer, Until We Read His Pull Request**\\
\\
**When experience doesn’t translate to expertise, and how one code review changed everything**](https://medium.com/@ThreadSafeDiaries/he-was-a-senior-developer-until-we-read-his-pull-request-2822831e35a8?source=post_page---read_next_recirc--d7a49c4d4786----0---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

Aug 3

[A clap icon5.7K\\
\\
A response icon179](https://medium.com/@ThreadSafeDiaries/he-was-a-senior-developer-until-we-read-his-pull-request-2822831e35a8?source=post_page---read_next_recirc--d7a49c4d4786----0---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

![RAG Without Embeddings? Here’s how OpenAI is doing this…with Code](https://miro.medium.com/v2/resize:fit:679/0*iOsZ4_h_gY8xu7lV.png)

[![Level Up Coding](https://miro.medium.com/v2/resize:fill:20:20/1*5D9oYBd58pyjMkV_5-zXXQ.jpeg)](https://medium.com/gitconnected?source=post_page---read_next_recirc--d7a49c4d4786----1---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

In

[Level Up Coding](https://medium.com/gitconnected?source=post_page---read_next_recirc--d7a49c4d4786----1---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

[Gaurav Shrivastav](https://medium.com/@gaurav21s?source=post_page---read_next_recirc--d7a49c4d4786----1---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

[**RAG Without Embeddings? Here’s how OpenAI is doing this…with Code**\\
\\
**How OpenAI Could Change the Way We Retrieve Information — Without Embeddings or Vector Databases with Colab Notebook**](https://medium.com/gitconnected/rag-without-embeddings-heres-how-openai-is-doing-this-45866cd5ddc6?source=post_page---read_next_recirc--d7a49c4d4786----1---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

Jun 11

[A clap icon580\\
\\
A response icon13](https://medium.com/gitconnected/rag-without-embeddings-heres-how-openai-is-doing-this-45866cd5ddc6?source=post_page---read_next_recirc--d7a49c4d4786----1---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

![Google Just Eliminated the AI Infrastructure Headache for $25/Month](https://miro.medium.com/v2/resize:fit:679/1*IRKSlK0Q7-siCmSOydtAGA.png)

[![Jannis](https://miro.medium.com/v2/resize:fill:20:20/1*AZ8boysRVFpu2_a7SzFXyA.png)](https://medium.com/@PowerUpSkills?source=post_page---read_next_recirc--d7a49c4d4786----2---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

[Jannis](https://medium.com/@PowerUpSkills?source=post_page---read_next_recirc--d7a49c4d4786----2---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

[**Google Just Eliminated the AI Infrastructure Headache for $25/Month**\\
\\
**Google just solved the biggest pain point for developers building AI solutions: the infrastructure complexity and cost barrier that comes…**](https://medium.com/@PowerUpSkills/google-just-eliminated-the-ai-infrastructure-headache-for-25-month-f96e565c2a1f?source=post_page---read_next_recirc--d7a49c4d4786----2---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

Aug 2

[A clap icon1.9K\\
\\
A response icon29](https://medium.com/@PowerUpSkills/google-just-eliminated-the-ai-infrastructure-headache-for-25-month-f96e565c2a1f?source=post_page---read_next_recirc--d7a49c4d4786----2---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

![Gemini CLI MCP Tutorial](https://miro.medium.com/v2/resize:fit:679/1*u3AGzMUgGpYgdsPeocyGfw.png)

[![Joe Njenga](https://miro.medium.com/v2/resize:fill:20:20/1*0Hoc7r7_ybnOvk1t8yR3_A.jpeg)](https://medium.com/@joe.njenga?source=post_page---read_next_recirc--d7a49c4d4786----3---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

[Joe Njenga](https://medium.com/@joe.njenga?source=post_page---read_next_recirc--d7a49c4d4786----3---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

[**Gemini CLI MCP Tutorial: Setup, Commands, & Practical Use (Step by Step Example)**\\
\\
**If you would like to set up Gemini CLI with any MCP server, this quick tutorial will guide you.**](https://medium.com/@joe.njenga/gemini-cli-mcp-tutorial-setup-commands-practical-use-step-by-step-example-b57f55db5f4a?source=post_page---read_next_recirc--d7a49c4d4786----3---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

Jun 30

[A clap icon172\\
\\
A response icon4](https://medium.com/@joe.njenga/gemini-cli-mcp-tutorial-setup-commands-practical-use-step-by-step-example-b57f55db5f4a?source=post_page---read_next_recirc--d7a49c4d4786----3---------------------024020a6_1bf6_4828_9f3e_ddc5857c7288--------------)

[See more recommendations](https://medium.com/?source=post_page---read_next_recirc--d7a49c4d4786---------------------------------------)

[Help](https://help.medium.com/hc/en-us?source=post_page-----d7a49c4d4786---------------------------------------)

[Status](https://medium.statuspage.io/?source=post_page-----d7a49c4d4786---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----d7a49c4d4786---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----d7a49c4d4786---------------------------------------)

[Press](mailto:pressinquiries@medium.com)

[Blog](https://blog.medium.com/?source=post_page-----d7a49c4d4786---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----d7a49c4d4786---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----d7a49c4d4786---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----d7a49c4d4786---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----d7a49c4d4786---------------------------------------)

reCAPTCHA

Recaptcha requires verification.

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)

protected by **reCAPTCHA**

[Privacy](https://www.google.com/intl/en/policies/privacy/) \- [Terms](https://www.google.com/intl/en/policies/terms/)
