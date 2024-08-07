# BioBERT for Named Entity Recognition

To train an NER model with BioBERT-v1.1 (base), run the command below.
Before training, please run `./preprocess.sh` to preprocess the datasets downloaded in `biobert-pytorch`

## Additional Requirements
- seqeval : Used for NER evaluation (`pip install seqeval`)

## Training
python run_ner.py \
    --data_dir ${DATA_DIR}/${ENTITY}/ \
    --labels ${DATA_DIR}/${ENTITY}/labels.txt \
    --model_name_or_path dmis-lab/biobert-base-cased-v1.1 \
    --output_dir ${SAVE_DIR}/${ENTITY} \
    --max_seq_length ${MAX_LENGTH} \
    --num_train_epochs ${NUM_EPOCHS} \
    --per_device_train_batch_size ${BATCH_SIZE} \
    --save_steps ${SAVE_STEPS} \
    --seed ${SEED} \
    --do_train \
    --do_eval \
    --do_predict \
    --overwrite_output_dir
```

## Evaluation Results For 30 EPOCH MODEL

### BioBERT

|                |    Test Precision (%)   |    Test Recall (%)   |    Test F1 (%)   |
|----------------|:-----------------------:|:--------------------:|:----------------:|
| NCBI-disease   |          85.4           |         89.2        |       87.3        |
