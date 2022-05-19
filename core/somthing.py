from connections import ConnectionToDatabase


author_id = ConnectionToDatabase.select_all(
                                            f"select id"
                                            f" from public.authors "
                                            f"where first_name "
                                            f"ilike '%{'jan'}%' "
                                            f"and "
                                            f"last_name "
                                            f"ilike '%{'pawe'}%' "
                                            f"limit 1",
                                            None)

print(author_id)