import time
from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_extract, col, avg, desc

start_time = time.time()

# Start Spark session
spark = SparkSession.builder.appName("Job Data Analysis").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

# Read the CSV file
df = spark.read.csv("job_descriptions.csv", header=True, inferSchema=False)

# Extract lower salary (e.g., from "$56K-$116K" -> 56000)
df = df.withColumn("Salary_Min", regexp_extract(col("Salary Range"), r"\$(\d+)K", 1).cast("int") * 1000)

# Drop rows where parsing failed
df = df.dropna(subset=["Salary_Min", "Job Title", "Company", "location"])

# Filter high-paying jobs
high_salary_jobs = df.filter(col("Salary_Min") > 1000)

# Show some filtered jobs
high_salary_jobs.select("Job Title", "Salary_Min", "location", "Company").show(10, truncate=False)

# Average salary by job title
avg_salary = high_salary_jobs.groupBy("Job Title") \
    .agg(avg("Salary_Min").alias("Average Salary")) \
    .orderBy(desc("Average Salary"))

print("Top 10 High Paying Roles:")
avg_salary.show(10, truncate=False)

# Count jobs by company
job_count = high_salary_jobs.groupBy("Company").count().orderBy(desc("count"))
print("Top Companies Hiring for High Salary Roles:")
job_count.show(10, truncate=False)

end_time = time.time()
print(f"\n✅ Execution Time: {end_time - start_time:.2f} seconds")
