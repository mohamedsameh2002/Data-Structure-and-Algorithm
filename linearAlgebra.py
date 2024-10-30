import numpy as np
# from sklearn.preprocessing import StandardScaler, MinMaxScaler
# from sklearn.decomposition import PCA
# from numpy.linalg import svd

# 1. الضرب الداخلي (Dot Product)
# print("1. الضرب الداخلي:")
# a = np.array([1, 2])
# b = np.array([3, 4])
# dot_product = np.dot(a, b)
# print(f"الضرب الداخلي بين {a} و {b} هو: {dot_product}\n")

# # 2. التحويلات (Transformations)
# print("2. التحويلات:")
# matrix = np.array([[1, 2], [3, 4]])

# # التحويل المنقول (Transpose)
# transpose_matrix = np.transpose(matrix)

# # التحويل المعكوس (Inverse)
# inverse_matrix = np.linalg.inv(matrix)

# print("المصفوفة الأصلية:")
# print(matrix)
# print("المصفوفة المنقولة:")
# print(transpose_matrix)
# print("المصفوفة المعكوسة:")
# print(inverse_matrix)
# print()

# 3. الانحدار (Regression)
print("3. الانحدار:")
X = np.array([[1, 2], [2, 3], [3, 4]])
y = np.array([2, 3, 4])

# إضافة عمود من الأحاديات لمصفوفة X
X_b = np.c_[np.ones((X.shape[0], 1)), X]

# حساب معاملات الانحدار
theta_best = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y

print("معاملات الانحدار:")
print(theta_best)
print()

# # 4. التحجيم والتقييس (Normalization and Scaling)
# print("4. التحجيم والتقييس:")
# data = np.array([[1, 2], [3, 4], [5, 6]])

# # التقييس القياسي (Standardization)
# scaler = StandardScaler()
# data_standardized = scaler.fit_transform(data)

# # التقييس بين 0 و 1 (Min-Max Scaling)
# scaler_minmax = MinMaxScaler()
# data_normalized = scaler_minmax.fit_transform(data)

# print("البيانات بعد التقييس القياسي:")
# print(data_standardized)
# print("البيانات بعد التقييس بين 0 و 1:")
# print(data_normalized)
# print()

# # 5. التحليل التمييزي (Dimensionality Reduction)
# print("5. التحليل التمييزي:")
# data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# # تطبيق PCA لتقليل الأبعاد إلى 2
# pca = PCA(n_components=2)
# data_reduced = pca.fit_transform(data)

# print("البيانات بعد تقليل الأبعاد:")
# print(data_reduced)
# print()

# # 6. التحويلات المثلثية (Matrix Factorizations)
# print("6. التحويلات المثلثية:")
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# # تطبيق تحليل القيمة المفردة (SVD)
# U, S, Vt = svd(matrix)

# print("U:")
# print(U)
# print("S:")
# print(S)
# print("Vt:")
# print(Vt)











# # تعريف المتجهات
# v1 = np.array([1, 2, 3])
# v2 = np.array([4, 5, 6])

# # 1. جمع المتجهات
# result_addition = v1 + v2
# print("جمع المتجهات:", result_addition)

# # 2. الضرب القياسي (Dot Product)
# dot_product = np.dot(v1, v2)
# print("الضرب القياسي:", dot_product)

# # 3. حساب الطول (Magnitude) لمتجه
# magnitude_v1 = np.linalg.norm(v1)
# print("طول المتجه v1:", magnitude_v1)

# # 4. حساب الفرق بين المتجهات
# difference = v1 - v2
# print("فرق المتجهات:", difference)
