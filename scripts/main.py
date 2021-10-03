import requests
import time
from bs4 import BeautifulSoup
import fileinput
import json
import concurrent.futures
biglist=[]
smalllist=[]


url =['https://www.qwiklabs.com/public_profiles/7ee15af9-9548-4a8e-8ae2-96654b3ad7bd', 'https://www.qwiklabs.com/public_profiles/4bbbe37b-4148-41d0-b6a1-1af698a73626', 'https://www.qwiklabs.com/public_profiles/86130b3f-d50b-481a-89d1-58a6b5d1d84c', 'https://google.qwiklabs.com/public_profiles/1038275a-925d-4ab6-9d88-a68f9b83a13b', 'https://www.qwiklabs.com/public_profiles/f84f9c5f-7274-473f-89f4-b6c4780ab67a', 'https://www.qwiklabs.com/public_profiles/285fd5bd-4931-4be3-aecd-b39f8ce9993b', 'https://googlecloud.qwiklabs.com/public_profiles/ceec7104-8ed1-439a-9cda-b77fd3de3c8f', 'https://www.qwiklabs.com/public_profiles/a65343f1-60f5-4b09-9181-14dee6e9a3e7', 'https://www.qwiklabs.com/public_profiles/b15b09ac-6c72-4b45-bc2e-7b088f8d0d39', 'https://www.qwiklabs.com/public_profiles/bbfbb09d-11c9-4450-8fe0-3cd25de9bb0e', 'https://www.qwiklabs.com/public_profiles/ea8c4ef4-b444-4a8e-9655-a007e91bbd0c', 'https://run.qwiklabs.com/public_profiles/e3533aec-de13-4938-baff-b929b06b7b02', 'https://www.qwiklabs.com/public_profiles/bc0328b8-6919-4fcc-bd4f-bea95aefa2c3', 'https://www.qwiklabs.com/public_profiles/4678d98e-e724-46cf-8569-3954888572e5', 'https://run.qwiklabs.com/public_profiles/10310a91-c8e4-4acc-a1a7-d3b55576911d', 'https://www.qwiklabs.com/public_profiles/e1c1722a-df52-4750-85fd-10c5d49ea266', 'https://www.qwiklabs.com/public_profiles/785f7d3f-c6e4-4b57-bfb6-dfa9f2fc8d43', 'https://www.qwiklabs.com/public_profiles/80a29744-034a-4acf-80e8-d865c43d4477', 'https://www.qwiklabs.com/public_profiles/d70e1909-313c-42af-92b8-9b4c70a30dba', 'https://www.qwiklabs.com/public_profiles/b7bbdd94-0f9b-4667-b853-7fe64cb5e8d9', 'https://google.qwiklabs.com/public_profiles/2c942b47-1ecf-4e6c-9748-29f8638f9d8e', 'https://www.qwiklabs.com/public_profiles/9786e0ce-053c-44a6-890c-8c33e654cef1', 'https://www.qwiklabs.com/public_profiles/54b90ec2-b403-4f70-9f68-ef9f6a69f89c', 'https://www.qwiklabs.com/public_profiles/46a33ddf-089a-4723-bad3-00386352ce68', 'https://www.qwiklabs.com/public_profiles/a0af74f4-7e21-49f5-b980-2d8b4d5b17c7', 'https://www.qwiklabs.com/public_profiles/8d4bf89d-decb-4adf-91f7-b2f7e53fda1b', 'https://www.qwiklabs.com/public_profiles/3412a194-0c46-4a21-b49f-84c9c9c4842e', 'https://www.qwiklabs.com/public_profiles/fe8f0bd2-4c06-4bf1-87c4-d86fc8cf702e', 'https://www.qwiklabs.com/public_profiles/61e55af5-188e-41c4-9203-7c1238c9a112', 'https://www.qwiklabs.com/public_profiles/d47429af-8af9-48e0-9973-1e13a2942465', 'https://www.qwiklabs.com/public_profiles/d699bed2-bb70-4375-b1c0-e5eac9ef87e5', 'https://www.qwiklabs.com/public_profiles/133f9889-1d03-4286-a77e-728d8e134663', 'https://www.qwiklabs.com/public_profiles/79c0911e-a1c1-48bf-b850-66d7f50614b6', 'https://www.qwiklabs.com/public_profiles/9fd8933c-b5e2-4905-a308-2255ab21cf39', 'https://www.qwiklabs.com/public_profiles/45cab90b-20ff-4164-ae63-e40a4845e66d', 'https://www.qwiklabs.com/public_profiles/6ca1f0ca-78a9-4e64-8519-410c5646f714', 'https://www.qwiklabs.com/public_profiles/6ce93825-1671-4431-9411-2a5ee1a88306', 'https://www.qwiklabs.com/public_profiles/cf274033-c0a9-4eba-a9fa-fc9042e88b09', 'https://www.qwiklabs.com/public_profiles/f1ac7df5-7517-4481-85a6-d8e21bc0d389', 'https://www.qwiklabs.com/public_profiles/064abf5d-04e5-43bc-8ea7-7b163329df31', 'https://www.qwiklabs.com/public_profiles/2c2c6429-9525-49c3-82cc-167b335d7c3c', 'https://www.qwiklabs.com/public_profiles/0f248eb1-f845-49f2-a47b-3aa187888e32', 'https://www.qwiklabs.com/public_profiles/0b751e58-c22e-464d-9a84-c5a4b17ddeeb', 'https://run.qwiklabs.com/public_profiles/1f164b8f-988a-4e20-a53c-dccaccc53729', 'https://www.qwiklabs.com/public_profiles/cb4c9aad-2207-4a58-87f1-031df54e960b', 'https://google.qwiklabs.com/public_profiles/88da641e-a2e5-4fef-973a-3af078c8101b', 'https://www.qwiklabs.com/public_profiles/3938dfeb-f55e-4914-a579-ecf9acbce498', 'https://www.qwiklabs.com/public_profiles/8996009b-8196-4b71-8f5a-8526ad534b82', 'https://www.qwiklabs.com/public_profiles/c2c3dbf8-465a-413a-af3f-cc8145079090', 'https://www.qwiklabs.com/public_profiles/7ebd0354-c382-4b7c-9062-1bd1bb73495a', 'https://www.qwiklabs.com/public_profiles/b98b0173-e11a-4f34-9538-241577dc4363', 'https://www.qwiklabs.com/public_profiles/7effc0ef-05d8-4e2a-8581-ce09579945fe', 'https://google.qwiklabs.com/public_profiles/ad814997-b312-4c2a-b0ab-b35c4c64e0b6', 'https://www.qwiklabs.com/public_profiles/488fd531-395f-4a3e-a8f9-807a5a2c1109', 'https://google.qwiklabs.com/public_profiles/55bfe417-7991-4669-8e21-94fdcc42be29', 'https://google.qwiklabs.com/public_profiles/20d4d794-5140-4736-affe-2367ffda5205', 'https://www.qwiklabs.com/public_profiles/cf0ef345-a9fe-4d55-8c72-25a800fba4dc', 'https://www.qwiklabs.com/public_profiles/80f58dc3-1e15-4b9c-875d-337e577d4e35', 'https://www.qwiklabs.com/public_profiles/a934ace7-c47d-40d8-b1a7-0fb02e7d7f08', 'https://google.qwiklabs.com/public_profiles/2d8a46cc-3cdb-4d6c-9f56-3eab584e3c37', 'https://www.qwiklabs.com/public_profiles/60cfae18-31d3-4dd0-9f20-4e42bcaeac0f', 'https://www.qwiklabs.com/public_profiles/6aea65d7-d087-42ed-9be2-d591877e45b3', 'https://www.qwiklabs.com/public_profiles/8a385c37-1142-4446-a322-905c34d3c7ee', 'https://google.qwiklabs.com/public_profiles/29bead40-cae5-4c82-8ad3-5d6702181a10', 'https://google.qwiklabs.com/public_profiles/15aa1d5d-b977-472f-817a-cb2f30926ba9', 'https://www.qwiklabs.com/public_profiles/7c42fb73-a3f8-4df8-b5fc-b7a6571966aa', 'https://www.qwiklabs.com/public_profiles/2ca8ce7d-19d9-4fac-8070-f4089257dd1c', 'https://www.qwiklabs.com/public_profiles/dee7b4c0-1421-4cb9-af73-6e02de7a4d51', 'https://www.qwiklabs.com/public_profiles/bdf20925-9fac-4f28-8bd2-9d7a8b16360f', 'https://www.qwiklabs.com/public_profiles/48c075fe-5c8b-4326-a37f-f6b54d563533', 'https://google.qwiklabs.com/public_profiles/d7137b28-109c-4158-9771-cbd817e5fd6e', 'https://www.qwiklabs.com/public_profiles/eb06eb32-88d8-48ab-92d3-9681b2bf04bb', 'https://www.qwiklabs.com/public_profiles/9435c638-c175-4d22-aae9-946696c514a1', 'https://run.qwiklabs.com/public_profiles/87ff8081-80f1-428a-9632-0398341ce3c1', 'https://www.qwiklabs.com/public_profiles/9ea03126-77f7-4073-bcc1-70abf434bd82', 'https://www.qwiklabs.com/public_profiles/504ec547-3d03-4ea0-93a9-8f8ed8cefc10', 'https://www.qwiklabs.com/public_profiles/4ab7a1aa-d045-44f2-90d6-71fa6e665109', 'https://www.qwiklabs.com/public_profiles/c6964e83-080b-4671-9276-e78b270c0003', 'https://google.qwiklabs.com/public_profiles/858e46a3-e848-41c4-a3ee-bdd0f2916eaa', 'https://google-run.qwiklabs.com/public_profiles/7db070b9-8d7c-4157-85fe-61f267ef87d5', 'https://www.qwiklabs.com/public_profiles/9c841504-a591-4825-9295-c9afe79eddd9', 'https://google.qwiklabs.com/public_profiles/252a900d-54f5-4f94-8a72-b4adc15a12aa', 'https://google.qwiklabs.com/public_profiles/31a187f5-59a6-451c-8a9f-c568ef2b354d', 'https://www.qwiklabs.com/public_profiles/12539dd4-ba62-4588-93ae-c7e69118ba1f', 'https://google.qwiklabs.com/public_profiles/60f7b7b6-5504-4a3f-a854-41a80a6691eb', 'https://www.qwiklabs.com/public_profiles/d0212339-1b79-4f7f-b8f3-0bd841b9a319', 'https://google.qwiklabs.com/public_profiles/929b2af7-8868-42f7-842c-f77c643b625d', 'https://www.qwiklabs.com/public_profiles/5b7472b2-2530-4d1d-93ca-e3e078f6372f', 'https://google.qwiklabs.com/public_profiles/fec51087-bc43-4ea6-bdb6-2b846d497f77', 'https://www.qwiklabs.com/public_profiles/bfd136aa-4282-4466-a739-3b0949dee6fd', 'https://www.qwiklabs.com/public_profiles/dfd70898-fdfb-4901-9ef2-ae10e6ca4395', 'https://www.qwiklabs.com/public_profiles/40e7f51f-eb0e-420c-b8ed-b83b749ef95b', 'https://www.qwiklabs.com/public_profiles/e786b636-ecd9-4a85-9f58-54592ceb64d7', 'https://www.qwiklabs.com/public_profiles/1b8e1cee-e832-4ad7-af49-a4bf9293ed46', 'https://www.qwiklabs.com/public_profiles/fdb495d5-0228-4130-bdd9-df8be69aab6d', 'https://google.qwiklabs.com/public_profiles/1ede595b-0a12-4f0a-babd-f81e8c595e60', 'https://www.qwiklabs.com/public_profiles/579d90ff-d917-4756-8147-fcf41c7f52e2', 'https://www.qwiklabs.com/public_profiles/8e1bf8b7-9293-4238-8714-97767a9d7a88', 'https://google.qwiklabs.com/public_profiles/328fd94c-3db9-4dac-a552-0b75b11bab12', 'https://www.qwiklabs.com/public_profiles/e3407803-779b-4bdd-bde4-e13d5a31a285', 'https://www.qwiklabs.com/public_profiles/d972eb27-b32f-4655-bbea-0f28e3c5a662', 'https://www.qwiklabs.com/public_profiles/8025af73-7145-4ea1-be86-301926c64ef2', 'https://run.qwiklabs.com/public_profiles/974c17bb-7807-4d34-a94c-ce26e7c6dc74', 'https://google.qwiklabs.com/public_profiles/8dd87fd0-57ad-45da-8cf4-906048f321e9', 'https://google.qwiklabs.com/public_profiles/f15708e8-cfcd-4c6c-8d1b-77010893d3ba', 'https://run.qwiklabs.com/public_profiles/514c91fa-874d-456a-aad1-d26961ce52d3', 'https://www.qwiklabs.com/public_profiles/a5a8ac6b-cfc5-44fb-8b0f-8afb070019a5', 'https://google.qwiklabs.com/public_profiles/1a5a42af-589e-496b-9e2e-a6fc70a52630', 'https://www.qwiklabs.com/public_profiles/ddf47dce-393e-4461-ad34-bbf4412704c0', 'https://www.qwiklabs.com/public_profiles/b29a2832-139e-466d-8404-bb6bb4b7f2d0', 'https://google.qwiklabs.com/public_profiles/1a632ffa-38cd-4a3b-8976-cad488c09974', 'https://www.qwiklabs.com/public_profiles/58eb0681-09ba-4f95-a22f-cb9fb1b2501f', 'https://google.qwiklabs.com/public_profiles/9e146c75-12d7-4e72-b0b3-d14e5474cabc', 'https://google.qwiklabs.com/public_profiles/e69a4764-c3b3-446b-b96d-9c193917835e', 'https://www.qwiklabs.com/public_profiles/cb0f4a40-e282-4c65-9581-c91a2297fb75', 'https://www.qwiklabs.com/public_profiles/1723f887-941c-4019-bf5d-aa32e370a54a', 'https://www.qwiklabs.com/public_profiles/3b8d858e-f3a9-4eb3-873d-5dfb43629cbf', 'https://google.qwiklabs.com/public_profiles/f661d37e-a14b-4f9c-acfa-86328abc91e2', 'https://www.qwiklabs.com/public_profiles/daacaf11-d88e-445e-b68c-e1e30ffa8fa2', 'https://www.qwiklabs.com/public_profiles/029ce26d-b8e8-4a66-b3e9-78084c5ee02c', 'https://www.qwiklabs.com/public_profiles/6c287fd3-b4ac-4e59-ad12-0d6a417dc464', 'https://www.qwiklabs.com/public_profiles/813acc46-3bab-4157-9b68-c3e16d7031c9', 'https://www.qwiklabs.com/public_profiles/fae46264-b583-42d1-8993-e3678ca3991b', 'https://www.qwiklabs.com/public_profiles/d3423719-c46a-4e20-ad58-66f9e99572fd', 'https://www.qwiklabs.com/public_profiles/fcc2cadd-e6c9-4761-9bba-814d3233c107', 'https://www.qwiklabs.com/public_profiles/58d896dc-efe8-4db4-b2a0-f02e517d1d5c', 'https://www.qwiklabs.com/public_profiles/94aa742c-7ce5-4960-b46b-78d4cac9764f', 'https://google.qwiklabs.com/public_profiles/0aec29a9-558a-458a-91da-6ec55d468d83', 'https://google.qwiklabs.com/public_profiles/e163484c-5958-4c68-98d8-bd3d6eef068c', 'https://www.qwiklabs.com/public_profiles/072cdee5-cbe8-4472-aa20-446f9c62c2a7', 'https://www.qwiklabs.com/public_profiles/113b3d6f-4460-4a0f-a46b-eddd22f85309', 'https://www.qwiklabs.com/public_profiles/2ff696c6-f4dc-418f-884d-c1188040e52a', 'https://www.qwiklabs.com/public_profiles/cddcb530-8dda-4b7c-9e12-84577fb33775', 'https://google.qwiklabs.com/public_profiles/94763196-ee44-430c-8df6-0eb9b088046b', 'https://google.qwiklabs.com/public_profiles/e51d6992-872e-457e-8431-1fc63b2d9a5b', 'https://google.qwiklabs.com/public_profiles/e22c340a-0e92-4af2-b70c-b88a9acc8f50', 'https://www.qwiklabs.com/public_profiles/63f0ff07-a0e7-43b5-8ecd-d21917e6afda', 'https://www.qwiklabs.com/public_profiles/8d05faa5-0fa5-40d2-9da2-19821bd94841', 'https://www.qwiklabs.com/public_profiles/40582cc7-8331-4edd-a7af-d371655cecbb', 'https://google.qwiklabs.com/public_profiles/79f1c560-50e0-496f-b99b-875a90e6ac2b', 'https://google.qwiklabs.com/public_profiles/13e365da-ed15-46ba-a984-76a46d8f66d1', 'https://google.qwiklabs.com/public_profiles/cb089f76-bd31-44a2-bfdc-dd008e39de53', 'https://www.qwiklabs.com/public_profiles/d8d4499d-5bde-466d-8b02-d673aea482a4', 'https://google.qwiklabs.com/public_profiles/aa8e6b67-cce7-4e0f-a2ab-08f24572b84d', 'https://google.qwiklabs.com/public_profiles/13a71a41-a0d1-49d4-b487-a1ae0ad73d37', 'https://www.qwiklabs.com/public_profiles/91e4d447-6bde-4b19-be75-5bbaec26573b', 'https://google.qwiklabs.com/public_profiles/307ff0d9-54eb-4ccc-a4e1-7ed99d2433a5', 'https://google.qwiklabs.com/public_profiles/65673352-d87a-4c8a-8020-bc719725e6be', 'https://google.qwiklabs.com/public_profiles/9e86fbf9-2c6d-41a2-8f9e-d12545d1189c', 'https://google.qwiklabs.com/public_profiles/f25745dc-ad0d-42dc-a1fb-24d0c2a7ed41', 'https://www.qwiklabs.com/public_profiles/c74e2463-409d-4e71-951d-461c067254ba', 'https://www.qwiklabs.com/public_profiles/fbe521f9-6915-47a3-b8d7-b6b224336573', 'https://google.qwiklabs.com/public_profiles/08834ba9-3fdc-49de-ab70-7792d13cb541', 'https://www.qwiklabs.com/public_profiles/38e42c96-0e8b-4b3d-8fa5-b27295ff2fff', 'https://www.qwiklabs.com/public_profiles/a1b2e0c4-3ccb-42a1-b139-1d6bfe8fe162', 'https://www.qwiklabs.com/public_profiles/e56a6d6c-984a-42fe-87bc-9029697ab4f5', 'https://www.qwiklabs.com/public_profiles/9254a78d-88d2-4af9-88b6-532dabe7f5f7', 'https://google.qwiklabs.com/public_profiles/2932d1fa-db0b-4df6-bdb3-0cecfe43a6b7', 'https://www.qwiklabs.com/public_profiles/a6fdbd1c-20c5-4b3b-ac37-cf75f36a1ad2', 'https://google.qwiklabs.com/public_profiles/e605b40c-80b8-4712-a559-71d3f134df65', 'https://google.qwiklabs.com/public_profiles/08687433-7596-45b6-bf6d-489d93510306', 'https://google.qwiklabs.com/public_profiles/00fa0d2e-5f8f-44a7-8db3-7dc8a882e2f5', 'https://www.qwiklabs.com/public_profiles/3d6944ef-5e4b-4046-bec2-ee3fdc6aedbb', 'https://www.qwiklabs.com/public_profiles/00ab6a7d-e716-4ee8-bac3-c80307e258f3', 'https://www.qwiklabs.com/public_profiles/58bda04b-b866-4fed-a618-a0ce5dcd7763', 'https://google.qwiklabs.com/public_profiles/6bbf1d7f-8050-427c-adb1-6440fa4b4361', 'https://google.qwiklabs.com/public_profiles/9883b378-5112-45a0-9ab7-35786d8087dc', 'https://google.qwiklabs.com/public_profiles/3b350234-aca6-48a3-8f11-9e85700ead37', 'https://google.qwiklabs.com/public_profiles/b8e443c9-7cd4-4fb2-bf05-1c961a0f8ef2', 'https://www.qwiklabs.com/public_profiles/dcb7ade9-8e88-45cc-b104-893862aeec1c', 'https://google.qwiklabs.com/public_profiles/9f3e444f-6ca0-488a-b0ec-5bed87890283', 'https://www.qwiklabs.com/public_profiles/63e0d5b2-b358-4ea4-83aa-5ab07f1db978', 'https://google.qwiklabs.com/public_profiles/30e79835-2313-44b9-b601-8f0600d1599d', 'https://www.qwiklabs.com/public_profiles/61121bd7-1f83-4307-bdf5-f373178e0a0a', 'https://www.qwiklabs.com/public_profiles/e55575b3-3158-4679-9481-b76aa79f6b72', 'https://www.qwiklabs.com/public_profiles/76efe255-1a85-4907-adaf-65b8fd31b0b9', 'https://run.qwiklabs.com/public_profiles/ece95284-15e8-476c-96a7-75b5182d843c', 'https://www.qwiklabs.com/public_profiles/9327694e-a74a-4d69-babc-0c7eb61373c7', 'https://www.qwiklabs.com/public_profiles/055a3fc7-c90f-44e2-a950-5ab647a34230', 'https://google.qwiklabs.com/public_profiles/cd766d6a-b0d2-4b73-9239-3605a5daac59', 'https://www.qwiklabs.com/public_profiles/65cc5221-df3b-446c-8ed1-bd4a6f2ebe16', 'https://www.qwiklabs.com/public_profiles/109c02a6-fd44-4c82-8926-44c0f846f18f', 'https://www.qwiklabs.com/public_profiles/48c4382a-e304-44cc-aec4-299e25c725be', 'https://google.qwiklabs.com/public_profiles/454fcbf8-fb8d-474d-a01d-fccb7881cfda', 'https://google.qwiklabs.com/public_profiles/44b61036-ca85-44f8-8255-b2066a8c6109', 'https://www.qwiklabs.com/public_profiles/98fd4568-3144-4674-b69b-0805bf2cebdb', 'https://www.qwiklabs.com/public_profiles/fa25253d-4f3f-47d6-9e58-8e553cadf45a', 'https://google.qwiklabs.com/public_profiles/f360bc81-eec1-4677-a6eb-2cb8ee2d14fd', 'https://www.qwiklabs.com/public_profiles/4374de1d-6254-4c2f-94c4-cfeff3c7991c', 'https://google.qwiklabs.com/public_profiles/589080e3-a67d-4247-8c11-4ac25a9784fd', 'https://google.qwiklabs.com/public_profiles/413e9af0-1ff4-419c-9fcb-cdf89a0ab6cf', 'https://www.qwiklabs.com/public_profiles/26b4abb6-8263-4b23-86f2-6e4be05a5263', 'https://www.qwiklabs.com/public_profiles/5a79972b-943a-4060-a28d-3f83c82f459c', 'https://google.qwiklabs.com/public_profiles/eae8758c-a9bb-4bba-8c79-a7dd26426b0a', 'https://www.qwiklabs.com/public_profiles/23cc515d-73ee-4ef0-bf22-2edeb234c56f', 'https://google.qwiklabs.com/public_profiles/f850b1dd-6e58-4849-b2ab-ad88e11f41b0', 'https://google-run.qwiklabs.com/public_profiles/a838dcd4-ac49-42dd-877c-2d438efbab9c', 'https://www.qwiklabs.com/public_profiles/3c60e5a7-5b2c-40f6-b9ef-da03610d83a9', 'https://google.qwiklabs.com/public_profiles/7427167c-9403-4058-9038-3c25b2153e42', 'https://www.qwiklabs.com/public_profiles/c4e5f7ff-9d17-4fae-8a87-c660709a6019', 'https://google.qwiklabs.com/public_profiles/bf04631d-ce44-455f-977e-5e3a970d587b', 'https://www.qwiklabs.com/public_profiles/f070562b-bff2-4a18-9493-882190e4f375', 'https://www.qwiklabs.com/public_profiles/813acf9c-703c-4428-86af-e3994cb0792a', 'https://google.qwiklabs.com/public_profiles/2b90ac67-0694-495a-b289-79417c7497b3', 'https://www.qwiklabs.com/public_profiles/5264f207-ce93-4862-8ba4-90f4af3ca08f', 'https://www.qwiklabs.com/public_profiles/b6fe3b00-e801-48a2-b8fe-c1ac99cc41d5', 'https://www.qwiklabs.com/public_profiles/8b66abf6-5de6-45b3-94d4-1e9d1d06e34c', 'https://www.qwiklabs.com/public_profiles/51832b68-616a-4ce1-ac52-9714fa84d40d', 'https://www.qwiklabs.com/public_profiles/1b9495ee-cec6-43b9-8088-9c9f9d85851d', 'https://www.qwiklabs.com/public_profiles/d4b9f390-f3c6-40a3-9483-f92fc44dff37', 'https://www.qwiklabs.com/public_profiles/a96c32da-b49e-4cb5-8008-8e411778eccb', 'https://www.qwiklabs.com/public_profiles/d418c260-217f-47c1-990f-ad4e0181c73f', 'https://www.qwiklabs.com/public_profiles/408a6a47-8d20-42f2-8a46-0ab0f8f9d065', 'https://www.qwiklabs.com/public_profiles/ce791846-49a9-4c83-bac1-c4ac6eac15b2', 'https://www.qwiklabs.com/public_profiles/529f0c08-1e83-4a1f-a1b3-e307a34ab1d0', 'https://www.qwiklabs.com/public_profiles/d8de0ea0-cdf4-4738-a66f-0c644a8c91a6', 'https://www.qwiklabs.com/public_profiles/1524df55-9259-47d5-a5d4-a6041633ddc5', 'https://www.qwiklabs.com/public_profiles/3ee772d7-9cfc-47aa-b441-280e6020af67', 'https://www.qwiklabs.com/public_profiles/7a1a9a95-93b3-4560-83ba-4aa50cfa7422', 'https://www.qwiklabs.com/public_profiles/3910e81d-2829-4107-9e6b-231b0800d5ca', 'https://www.qwiklabs.com/public_profiles/5f287464-3285-4aa1-ba27-c21b17961e41', 'https://www.qwiklabs.com/public_profiles/c5735507-f117-467b-88ae-d77efeeeacec', 'https://google.qwiklabs.com/public_profiles/bb939752-00bd-44a5-adf9-a63561c6a560', 'https://www.qwiklabs.com/public_profiles/a0e6520a-f332-494c-83bc-5fb164492a32', 'https://www.qwiklabs.com/public_profiles/462c8bba-b8bf-4331-949a-af306cf690c0', 'https://www.qwiklabs.com/public_profiles/7fa09300-72f8-4948-a837-0441993cb407', 'https://www.qwiklabs.com/public_profiles/c594e95f-4d8e-4a1a-b28a-831f99b9801a', 'https://run.qwiklabs.com/public_profiles/c32eaa68-32d0-46a9-8bf0-a82bfe3c5ca2', 'https://www.qwiklabs.com/public_profiles/0f3d13cd-fe6f-4b73-8ce1-9014a192d4a3', 'https://google-run.qwiklabs.com/public_profiles/c0f89bca-d5ff-4060-b610-e80524401993', 'https://google.qwiklabs.com/public_profiles/45233209-ff9b-4c38-950f-d92090c2d493', 'https://www.qwiklabs.com/public_profiles/17de858b-1b4f-43d5-a421-fe3bde127e40', 'https://google.qwiklabs.com/public_profiles/c7930b7a-6ef3-421c-8684-19478e7df84d', 'https://www.qwiklabs.com/public_profiles/a8c8f5f7-2ed7-4bf8-9899-2299fa990c7a', 'https://www.qwiklabs.com/public_profiles/ceaccf60-e0a0-454a-98aa-76db87df13ec', 'https://www.qwiklabs.com/public_profiles/222fb6fc-4c75-4c0e-8640-83a1c8299f81', 'https://google.qwiklabs.com/public_profiles/3439cea8-fdf3-4e08-bac4-f60be634211b', 'https://google.qwiklabs.com/public_profiles/0c54637e-6a1c-41e0-bab1-cf3987218e7f', 'https://www.qwiklabs.com/public_profiles/9f535a1b-80e5-4079-b697-ffd380391a0f', 'https://www.qwiklabs.com/public_profiles/4a420588-c714-4b58-aeb4-1b9499e866ad', 'https://www.qwiklabs.com/public_profiles/77a85d6f-c9c7-4685-96dd-e5c3e4071f2b', 'https://google.qwiklabs.com/public_profiles/b861fba2-c603-4670-84af-9dfd3fb6d04c', 'https://google.qwiklabs.com/public_profiles/bfc87d75-a88b-43d9-ad6f-34221a97a017', 'https://www.qwiklabs.com/public_profiles/351dc5b8-9c55-4991-bd2a-a202065258d2', 'https://www.qwiklabs.com/public_profiles/21f51bd0-bbf6-4792-a540-97d0438ead62', 'https://www.qwiklabs.com/public_profiles/971cb1ee-31fe-4e1a-bab7-c5f8c2e2f611', 'https://www.qwiklabs.com/public_profiles/80d27db6-9044-49f2-b128-9a8f9eda9012', 'https://google.qwiklabs.com/public_profiles/ca41797b-ad27-4431-9dee-ac28fe583a50', 'https://google.qwiklabs.com/public_profiles/6b355a4f-691e-46d4-af5e-92e6612a0210', 'https://www.qwiklabs.com/public_profiles/62f406f2-a964-4681-a150-40e0aaf2907f', 'https://google.qwiklabs.com/public_profiles/48a298da-8845-4265-8540-966d3903b754', 'https://google.qwiklabs.com/public_profiles/a9537bcb-7598-4998-92fb-28ae5a8818a4', 'https://www.qwiklabs.com/public_profiles/5787f075-b482-4532-aada-5af9f3374161', 'https://google.qwiklabs.com/public_profiles/fbb5150f-171d-45db-a645-93c793ce18d9', 'https://www.qwiklabs.com/public_profiles/c7014966-d3b9-4431-b027-02e419bf89d4', 'https://www.qwiklabs.com/public_profiles/56527460-b399-43c7-b3b9-e801828df93c', 'https://www.qwiklabs.com/public_profiles/ea63a753-208e-4bd9-a988-e3ff4cfd01f5', 'https://www.qwiklabs.com/public_profiles/2e46c767-2e2d-4295-8a08-1d91613681e7', 'https://www.qwiklabs.com/public_profiles/9eac32ab-1e4f-427b-a239-e80acab38a84', 'https://www.qwiklabs.com/public_profiles/ead5c7e8-731b-4c8b-aaa8-3fdae17a2e4c', 'https://www.qwiklabs.com/public_profiles/3c70a4ea-7e34-4b9d-a718-e77e26979884', 'https://www.qwiklabs.com/public_profiles/7e3c1e4e-4da6-4d07-afad-c75fe8f6c91b', 'https://www.qwiklabs.com/public_profiles/39efc0fb-f272-4158-ab7a-0e1b36fb2f25', 'https://google.qwiklabs.com/public_profiles/af57d767-67dc-4bef-9849-a3298198907b', 'https://google.qwiklabs.com/public_profiles/cd9f0f74-2bdc-4ab7-ac63-86aa7a7775bd', 'https://www.qwiklabs.com/public_profiles/3c41d988-6738-4a50-ba6a-83c1a274fa6d', 'https://google.qwiklabs.com/public_profiles/b481ec77-0315-4d71-a0fc-197b16604fca', 'https://google.qwiklabs.com/public_profiles/2773ee6a-1f5f-4f95-aa07-bee6340bd223', 'https://www.qwiklabs.com/public_profiles/da9ba94f-08d1-47d8-a050-4a30e1f02d51', 'https://google.qwiklabs.com/public_profiles/32626d84-bd05-4ed7-b85a-28e9a8e0a1fd', 'https://google.qwiklabs.com/public_profiles/b559f3f9-1d4e-4300-a64d-3100bc8eb4d4', 'https://google.qwiklabs.com/public_profiles/7af9e6e7-5ff2-4ef8-b963-2cc767be9657', 'https://www.qwiklabs.com/public_profiles/8b67f1f7-a0b6-474c-aa20-ea11f523cb74', 'https://www.qwiklabs.com/public_profiles/5cebb6ef-cd94-44e6-a692-3440edc08e66', 'https://www.qwiklabs.com/public_profiles/b221d807-047e-4c02-a873-c7ee277fe9b6', 'https://www.qwiklabs.com/public_profiles/7243fa76-edaa-48aa-8d38-dc7e24c4b496', 'https://www.qwiklabs.com/public_profiles/e55bf1ad-3e64-473b-af80-f92f8c755cc5', 'https://google.qwiklabs.com/public_profiles/4a151f43-ae8b-435f-beb2-9dbd068d0be8', 'https://www.qwiklabs.com/public_profiles/f9696045-3707-48a6-b711-04073d758612', 'https://google.qwiklabs.com/public_profiles/01a8a475-05e6-4693-9dee-85fc3841034d', 'https://www.qwiklabs.com/public_profiles/e01d1150-61cd-44ca-9382-c6513ece3949', 'https://google.qwiklabs.com/public_profiles/2d127e01-73cc-4695-8982-400c4eeb4e88', 'https://run.qwiklabs.com/public_profiles/16566734-cab7-45ec-b071-2ca58a5a7f4c', 'https://www.qwiklabs.com/public_profiles/3a78ae1c-5cef-4477-bf35-040acedf1a93', 'https://www.qwiklabs.com/public_profiles/fa46aa6c-2d3f-488a-82e1-913b686555bc', 'https://www.qwiklabs.com/public_profiles/88151669-6810-4e92-b366-e5a5b2875ba1', 'https://google.qwiklabs.com/public_profiles/3dfe5747-a95f-4d41-949d-394d3b7cf58d', 'https://www.qwiklabs.com/public_profiles/fd654d32-893b-4124-9678-17134a5abf98', 'https://google.qwiklabs.com/public_profiles/aee2c808-05d3-4be1-a232-2b782d7c3cf9', 'https://google.qwiklabs.com/public_profiles/1ddb6a87-4245-429a-83a4-cdae4b21e4c3', 'https://google.qwiklabs.com/public_profiles/68c8e59c-0caf-4185-8e93-8f04f4022738', 'https://google.qwiklabs.com/public_profiles/cbaf7ae0-90bd-49b0-9ba8-840a177d7eda', 'https://www.qwiklabs.com/public_profiles/883d841f-7827-4e17-918f-a814fa95df6d', 'https://www.qwiklabs.com/public_profiles/4981f1ea-bfda-44bd-bcdf-ac8c1112f346', 'https://www.qwiklabs.com/public_profiles/be00ff2e-891e-4375-b606-7cf8c728835e', 'https://www.qwiklabs.com/public_profiles/580bf244-4d2e-41e6-9978-7681e4583ffa', 'https://google.qwiklabs.com/public_profiles/6ccec6aa-40e7-4022-a69a-85cb9d30f73c', 'https://www.qwiklabs.com/public_profiles/9b619e41-cd9a-4548-b258-a0cd171ca98d', 'https://www.qwiklabs.com/public_profiles/fe68acfa-106c-4779-8c80-95c1a1ed7ecf', 'https://google.qwiklabs.com/public_profiles/92a403d0-f1c0-4e98-af29-737d377ceb9d', 'https://www.qwiklabs.com/public_profiles/954523de-6180-48fd-b35c-21d1b535b679', 'https://www.qwiklabs.com/public_profiles/49e45076-e6ce-4ba9-98cd-ffe9675e5cf9', 'https://google.qwiklabs.com/public_profiles/0feb07c4-ddf7-4bb0-850c-041189984b76', 'https://google.qwiklabs.com/public_profiles/88697afa-41b9-45c9-9c58-c788d8b61710', 'https://www.qwiklabs.com/public_profiles/e50618d8-4385-4eea-8617-64c1277ef982', 'https://google.qwiklabs.com/public_profiles/07c20006-894e-478e-b534-2b5b5135167c', 'https://run.qwiklabs.com/public_profiles/323c9294-3520-4e8e-8f59-55d06529b838', 'https://google.qwiklabs.com/public_profiles/71bdf12c-72a9-485f-b00c-6b46cb548bc6', 'https://www.qwiklabs.com/public_profiles/e9874d61-3b37-4fc6-bc51-d4df28f0cb00', 'https://google-run.qwiklabs.com/public_profiles/88d250bb-dc2b-439c-9801-f23e4ae62031', 'https://google.qwiklabs.com/public_profiles/78f8d3f2-b24e-4957-a410-88f2b7f93124', 'https://www.qwiklabs.com/public_profiles/fb7196c3-7c9c-49a4-87af-09d8f6725497', 'https://www.qwiklabs.com/public_profiles/597e87e1-706d-46ff-8848-d80cfa977061', 'https://run.qwiklabs.com/public_profiles/49586490-60b0-4ae5-94d3-b6d80cde9680', 'https://www.qwiklabs.com/public_profiles/792fd446-6410-4d62-a103-5cd90e5709d8', 'https://www.qwiklabs.com/public_profiles/0b9503b2-573a-4d56-adc6-a7d52eba2d10', 'https://www.qwiklabs.com/public_profiles/ee9de3a7-9a33-45d5-b782-492c786f4564', 'https://google.qwiklabs.com/public_profiles/53f27029-4e63-497a-b29a-ecfd798fd8cd', 'https://google.qwiklabs.com/public_profiles/1ae33fc7-6f6d-46a8-a500-ebca3d7d7d10', 'https://www.qwiklabs.com/public_profiles/dd670a87-c7a7-405a-89a2-ec71b8a76aed', 'https://google.qwiklabs.com/public_profiles/923e2e53-edc2-429e-8b8d-f712ccf410fd', 'https://www.qwiklabs.com/public_profiles/10bf988c-cfd9-4c8f-a728-82ae733ebd13', 'https://google.qwiklabs.com/public_profiles/18bbadfb-e55b-4ce8-82b5-3d65cac5076a', 'https://www.qwiklabs.com/public_profiles/1718d7ab-5d6a-42d9-9e5f-fe76d2f7062e', 'https://www.qwiklabs.com/public_profiles/4bffd6bc-63d5-4777-9592-0bb63d01c426', 'https://www.qwiklabs.com/public_profiles/4bb5c2b6-db2b-43a2-ac71-10d0b46b8a81', 'https://www.qwiklabs.com/public_profiles/9b3d35c4-fb38-407b-bec7-cb5943aca782', 'https://google.qwiklabs.com/public_profiles/8a661f37-5ff3-4bf1-9d62-107180cbbdeb', 'https://google.qwiklabs.com/public_profiles/588a3b53-fab1-49bf-9ad4-125901240fe2', 'https://www.qwiklabs.com/public_profiles/cc5143b0-6eb1-4184-b0bc-3f1a2afbc5f5']




track1=[
    'Create and Manage Cloud Resources',
    'Perform Foundational Infrastructure Tasks in Google Cloud',
    'Set Up and Configure a Cloud Environment in Google Cloud',
    'Deploy and Manage Cloud Environments with Google Cloud',
    'Build and Secure Networks in Google Cloud',
    'Deploy to Kubernetes in Google Cloud'
    ]
track2 = [
    'Create and Manage Cloud Resources',
    'Perform Foundational Data, ML, and AI Tasks in Google Cloud',
    'Insights from Data with BigQuery',
    'Engineer Data in Google Cloud',
    'Integrate with Machine Learning APIs',
    'Explore Machine Learning Models with Explainable AI'
    ]

def data_scraping (url):
    start_thread(url)

def data_gathering(link):
    #print("gathering data")
    tempdic = {}
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    #print(soup)
    alltracks = []
    track1completed = []
    track2completed = []
    profile = soup.findAll('h1', attrs = {'class':'ql-headline-1'})[0]
    #print(profile.text)
    name = profile.text.split('\n')[1]
    #print(name)
    profile = soup.findAll('ql-avatar', attrs = {'class':'l-mbl'})[0]
    #print(profile['src'])
    dp = profile['src']

    """
    tlab = profile.p.text
    labsnum = tlab.split()
        tempdic['labsattempted'] = 0
    """
    """
    profile = soup.findAll('span', attrs = {'class':'ql-subhead-1 l-mts'})
    #print(profile)
    for element in profile:
        #print(element.text.split('\n')[1])
        skillbadge = element.text.split('\n')[1]
        #alltracks.append(skillbadge)
        #print(skillbadge)
        if skillbadge in track1:
            track1completed.append(skillbadge)
        if skillbadge in track2:
            track2completed.append(skillbadge)

    print(alltracks)
    for skillbadge in alltracks:
        if skillbadge in track1:
            track1completed.append(skillbadge)
    for skillbadge in alltracks:
        if skillbadge in track2:
            track2completed.append(skillbadge)
    """
    profile = soup.findAll('div', attrs = {'class':'profile-badge'})
    #print(profile)

    for element in profile:
        key = element.findAll('span', attrs = {'class':'ql-subhead-1 l-mts'})[0]
        key2 = key.text.split('\n')[1]
        value = element.findAll('span', attrs = {'class':'ql-body-2 l-mbs'})[0]
        value2 = value.text.split('\n')[1]
        value3 = value2.split('Earned')[1]
        value4 = value3.split(" ")
        date = []
        for i in value4:
            if i!= '':
                date.append(i)
        #print(date)

        if date[0] == 'Sep':
            check = date[1].split(',')[0]
            if int(check) >= 22:
                #print(key2,date[1])
                if key2 in track1:
                    track1completed.append(key2)
                if key2 in track2:
                    track2completed.append(key2)
        elif date[0] == 'Oct':
            #print(date)
            check = date[1].split(',')[0]
            #print(check)
            if int(check) <= 27:
                #print(date)
                #print(key2,date[1])
                if key2 in track1:
                    track1completed.append(key2)
                if key2 in track2:
                    track2completed.append(key2)


        #print(key2,date)
    #print(track1completed,track2completed)


    #print(track1completed)
    #print(track2completed)
    tempdic['qlabid'] = link
    tempdic['id'] = len(biglist)+1
    tempdic['name'] = name
    tempdic['dp'] = dp
    tempdic['track1'] = track1completed
    tempdic['track2'] = track2completed
    tempdic['lentrack1'] = len(track1completed)
    tempdic['lentrack2'] = len(track2completed)
    #if tempdic['lentrack1'] == 6 or tempdic['lentrack2'] == 6:
    #id+=1
        #print(id)
    tempdic['qcomplete_no'] = len(track1completed) + len(track2completed)
    biglist.append(tempdic)
    if tempdic['qcomplete_no']!=0:
        print(tempdic['name']," got ",tempdic['qcomplete_no']," skill badges")
        #print("data saved")
    else:
        #print(tempdic['name']," got ",tempdic['qcomplete_no']," skill badges")
        pass

def data_saving (biglist):
    #num = 0

    tk1 = 0
    tk2 = 0
    tkt = 0
    tkb = 0
    for tempdic in biglist:
        if tempdic['qcomplete_no']!=0:
            smalllist.append(tempdic)

        x = int(tempdic['lentrack1'])
        y = int(tempdic['lentrack2'])
        """
        z = int(tempdic['labsattempted'])
        if z>=35:
            total_lab+=1
            #if x<5 and y<6:
            #    print(tempdic['name'],"did",tempdic['labsattempted'], "and got",x,"in track 1 and",y,"in track 2")
        """
        if x==6:
            tk1+=1
        if y==6:
            tk2+=1
        if x==6 or y==6:
            #print(tempdic['name'])
            tkt+=1
        if x==6 and y==6:
            tkb +=1


    print("Number of people completed track 1 : ",tk1)
    print("Number of people completed track 2 : ",tk2)
    print("Number of people completed atleast 1 track : ",tkt)
    print("Number of people completed both tracks : ",tkb)

    mile1 = (tkt/75)*100
    mile2 = (tkb/50)*100

    print("Milestone 1 completed : ",mile1,"%")
    print("Milestone 2 completed : ",mile2,"%")



    #print("Number of people may complete atleast 1 track  : ",total_lab)
    #print("number of people completed atleast one track ",num)
    #print(res)
    res = sorted(smalllist, key = lambda x: x['qcomplete_no'], reverse=True)
    print("number of people started : ",len(res))
    with open("my.json","w") as f:
        json.dump(res,f,indent=4)
    f.close()


def start_thread(url2):
    threads = 10
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(data_gathering, url2)
    data_saving (biglist)

def main(url):
    data_scraping (url)

if __name__ == '__main__':
    t0 = time.time()
    #id = 0
    print("started")
    main(url)
    t1 = time.time()
    print(f"{t1-t0} seconds to download {len(url)} profile.")
    #print("number of people completed atleast one track",id)
