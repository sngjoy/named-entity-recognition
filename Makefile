run-db:
	docker run -p 5432:5432 --name db -e POSTGRES_PASSWORD=password -e POSTGRES_DB=spacy_ner -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres
